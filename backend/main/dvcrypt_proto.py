import socket
import datetime
from Crypto.Hash import MD2

dvcrypt_command = {'login_getinfo': 0x10,       # Get salt from server
                   'login_try': 0x11,           # Try login
                   'log_out': 0x12,             # Log out
                   'totals_get': 0x40,          # Get subscribers or bouquet
                   'data_get': 0x41,            # Get bouquet detail
                   'subscriber_get': 0x33,      # Get subscriber info
                   'subscriber_set': 0x34}      # Set subscriber info


class DVCryptError(Exception):
    def __init__(self, message, server_result):
        self.message = message
        self.result = server_result

    def __str__(self):
        str = self.message
        command = ''
        for cmd, cmd_num in dvcrypt_command.items():
            if cmd_num == self.result['cmd']:
                command = cmd
        str += '\nServer return result result: \ncmd = {}'.format(command if command else self.result['cmd'])
        str += '\ndata = {}'.format(self.result['data'])
        return str


class Unknown(DVCryptError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        str = self.message
        return str


class UnknownData(DVCryptError):
    pass


class WrongCommandFormat(DVCryptError):
    pass


class LoginFailed(DVCryptError):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class DVCrypt(object):
    """ Class for operate with DVCrypt server """

    __size = 65547                      # Max message size
    __sync = [0xE2, 0x5A, 0xA5, 0xE4]   # Synchronization sequence described in API
    __sock = 0                          # Socket to communicate with server

    def __init__(self, ip, port):
        """
        Bind IP and PORT of DVCrypt server


        :param ip: ip string
        :type ip: string
        :param port: port number
        :type port: int
        """
        self.__ip = ip
        self.__port = port

    def connect(self):
        """ Connect to the server """
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__sock.connect((self.__ip, self.__port))

    def disconnect(self):
        """ Close socket """
        self.__sock.close()

    @staticmethod
    def __int_to_bytelist(value):
        """
        Convert int value to 4 bytes list


        :param value: integer number less when 32 bit
        :type value: int
        :return: list of 4 byte represented an integer value
        :rtype: list[int]
        :raise ValueError: When value < 0 or > 2147483647
        """
        if value < 0 or value > 2147483647:
            raise ValueError("value must be in range 0 .. 2.14e9")

        return [value & 0x000000FF, (value & 0x0000FF00) >> 8, (value & 0x00FF0000) >> 16,
                (value & 0xFF000000) >> 32]

    @staticmethod
    def __check_status(ans):
        """

        :param ans: server returned message
        :type ans: dict[str,any]
        :return: server status true - command accepted false - server busy
        :rtype: bool
        :raise WrongCommandFormat: When server return ERROR status
        :raise UnknownData: Unexpected server status
        """
        try:
            if ans['status'] == 0x00:
                return True
            elif ans['status'] == 0x01:
                return False
            elif ans['status'] == 0x02:
                raise WrongCommandFormat('Error command format', ans)
            else:
                raise UnknownData('Unknown Error', ans)
        except KeyError:
            raise UnknownData('Unknown Error. Status field is missing', ans)

    def send_command(self, cmd, addr=0x00, uid=(0x00, 0x00, 0x00, 0xA5), data=(), timeout=3):
        """
        Send command to the DVCrypt server and parse a result

        :param cmd: command from dvcrypt_command dict
        :type cmd: str
        :param addr: scrambler address 0x00 if command send for server
        :type addr: int
        :param uid: unique id of command 4 bytes
        :type uid: tuple
        :param data: command internal data list of bytes
        :type data: list[int]
        :param timeout: server waiting timeout in seconds
        :type timeout: int
        :return: parsed server data in dict
        :rtype: dict[str, any]
        """
        if len(data) > 65535:
            raise Exception('Len must be <65535')
        message = self.__sync[::-1]
        message.append(dvcrypt_command[cmd])
        message.append(addr)
        message.append(len(data) & 0x00FF)
        message.append((len(data) & 0xFF00) >> 8)
        message += uid[::-1]
        message += data
        ret = dict()
        start_time = datetime.datetime.now()
        timeout_d = datetime.timedelta(seconds=timeout)
        while True:
            self.__sock.send(bytes(message))
            data = self.__sock.recv(self.__size)
            if data and len(data) > 11:
                ret['cmd'] = data[4]
                ret['status'] = data[5]
                ret['len'] = (data[7] << 8) + data[6]
                ret['uid'] = data[8:12][::-1]
                ret['data'] = data[12:]
            else:
                raise Unknown('Server do not return a data')
            if self.__check_status(ret):
                break
            else:
                if datetime.datetime.now() - start_time < timeout_d:
                    continue
                else:
                    raise TimeoutError('Server do not answer in time {} seconds'.format(timeout))
        return ret

    def _get_login_info(self):
        """
            Get server salt for calculate credentials


            :return: salt list of 8 bytes
            :rtype: bytes
            :raise UnknownData: If server return a zero message - raise exception
            :raise UnknownData: if data field is missing
        """
        result = self.send_command('login_getinfo')
        try:
            if result['data'] and len(result['data']) > 8:
                return result['data'][:8]
            else:
                raise UnknownData('Unknown Error: ', result)
        except KeyError:
            raise UnknownData('Unknown Error. Data field is missing', result)

    def login(self, user, pswd):
        """
        Login to server


        :param user: user name
        :type user: str
        :param pswd: password
        :type pswd: str
        :return: first byte of access right bit mask 1 - enabled 0 - disabled
        :rtype: int
        :raise LoginFailed: if login or passsword incorrect
        :raise UnknownData: if data field is missing
        """
        salt = self._get_login_info()
        h = MD2.new()
        h.update(pswd.encode())
        h.update(salt)
        hd = h.digest()
        data = user.encode() + b'\x00'*(32 - len(user.encode())) + hd
        result = self.send_command('login_try', data=data)
        try:
            if result['data']:
                return int(result['data'][0])
            else:
                raise LoginFailed('Login failed. Login or password incorrect')
        except KeyError:
            raise UnknownData('Unknown Error. Data field is missing', result)

    def logout(self):
        """
            Log out


            :return: None
            :raise UnknownData: If server return a non zero message or data field is missing- raise exception
        """
        result = self.send_command('log_out')
        try:
            if result['data']:
                raise UnknownData('Unknown Error: ', result)
        except KeyError:
            raise UnknownData('Unknown Error. Data field is missing', result)

    def subscriber_get(self, start, stop):
        """
            Get subscribers data by card number. Batch read acceptable, recommended up to 50 per request


            :param start: start card number
            :type start: int
            :param stop: stop card number included
            :type stop: int
            :return: 16 bytes bit mask fo 128 bouquets 1-enable 0-disable
            :rtype: dict[int,bytes]
            :raise UnknownData: If server return a zero message or data field is missing- raise exception
        """
        dword_start = self.__int_to_bytelist(start)
        dword_stop = self.__int_to_bytelist(stop)
        data = []
        data += dword_start
        data += dword_stop

        result = self.send_command('subscriber_get', data=data)
        ret = {}
        try:
            if result['data'] and len(result['data']) == (stop - start + 1)*16:
                for i in range(0, stop - start + 1):
                    ret[start+i] = result['data'][i*16:(i+1)*16]
                return ret
            else:
                raise UnknownData('Unknown Error: ', result)
        except KeyError:
            raise UnknownData('Unknown Error. Data field is missing', result)

    def subscriber_set(self, start, stop, subscription, priority='low'):
        """
            Set subscribers data by card number. Batch write acceptable, recommended up to 50 per request


            :param start: start card number
            :type start: int
            :param stop: stop card number included
            :type stop: int
            :param subscription: 16 bytes bit mask fo 128 bouquets 1-enable 0-disable one for all cards in range
            :type subscription: bytes
            :param priority: Operation priority 'low' / 'high'
            :type priority: str
            :return: None
            :raise UnknownData: If server return a zero message or data field is missing- raise exception
        """
        dword_start = self.__int_to_bytelist(start)
        dword_stop = self.__int_to_bytelist(stop)
        data = []
        data += dword_start
        data += dword_stop
        if priority == 'low':
            data.append(0x00)
        else:
            data.append(0x01)
        data += list(subscription)
        result = self.send_command('subscriber_set', data=data)
        try:
            if result['data']:
                raise UnknownData('Unknown Error: ', result)
        except KeyError:
            raise UnknownData('Unknown Error. Data field is missing', result)

    def get_subscribers_count(self):
        """
        Get max subscribers count limited by license


        :return: max subscribers
        :rtype: int
        :raise UnknownData: If server return a zero message or data field is missing- raise exception
        """
        data = [0x03, 0x00, 0x00, 0x00, 0x00, 0x00]
        result = self.send_command('totals_get', data=data)
        ret = 0
        try:
            if result['data'] and len(result['data']) == 4:
                ret += result['data'][3] << 8 * 3
                ret += result['data'][2] << 8 * 2
                ret += result['data'][1] << 8 * 1
                ret += result['data'][0]
                return ret
            else:
                raise UnknownData('Unknown Error', result)
        except KeyError:
            raise UnknownData('Unknown Error. Data field is missing', result)

    def get_bouquet_count(self):
        """
        Get max bouquets count limited by server


        :return: max bouquets
        :rtype: int
        :raise UnknownData: If server return a zero message or data field is missing- raise exception
        """
        data = [0x01, 0x00, 0x00, 0x00, 0x00, 0x00]
        result = self.send_command('totals_get', data=data)
        ret = 0
        try:
            if result['data'] and len(result['data']) == 4:
                ret += result['data'][3] << 8 * 3
                ret += result['data'][2] << 8 * 2
                ret += result['data'][1] << 8 * 1
                ret += result['data'][0]
                return ret
            else:
                raise UnknownData('Unknown Error', result)
        except KeyError:
            raise UnknownData('Unknown Error. Data field is missing', result)

    def get_bouquet_detail(self, bouquet):
        """
        Return bouquet information

        :param bouquet: bouquet number
        :return: bouquet name and parental rate {'Name': 'Bouquet #1', 'parental': '10+'}
        :rtype: dict[str,str]
        :raise UnknownData: If server return a zero message or data field is missing- raise exception
        """
        dword_No = self.__int_to_bytelist(bouquet)
        data = [0x01]
        data += dword_No
        data += dword_No
        data.append(0x00)
        data += [0x00, 0x00, 0x00, 0x00]
        result = self.send_command('data_get', data=data)
        ret = dict()
        par = {0x00: 0,
               0x01: 4,
               0x02: 5,
               0x03: 6,
               0x04: 7,
               0x05: 8,
               0x06: 9,
               0x07: 10,
               0x08: 11,
               0x09: 12,
               0x0a: 13,
               0x0b: 14,
               0x0c: 15,
               0x0d: 16,
               0x0e: 17,
               0x0f: 18}
        try:
            if result['data'] and len(result['data']) == 20:
                ret['name'] = ''.join(result['data'][0:19].decode('ascii', errors="ignore").split('\x00'))
                ret['parental'] = par[result['data'][19]]
                return ret
            else:
                raise UnknownData('Unknown Error :', result)
        except KeyError:
            raise UnknownData('Unknown Error. Data field is missing', result)
