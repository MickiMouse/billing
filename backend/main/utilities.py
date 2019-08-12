from django.template.loader import render_to_string
from django.core.signing import Signer
from backend.settings import ALLOWED_HOSTS

signer = Signer()


def send_activation_notification(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user': user, 'host': host,
               'sign': signer.sign(user.email)}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body = render_to_string('email/activation_letter_body.txt', context)
    user.email_user(subject, body)


def send_request_reset_password(user):
    if ALLOWED_HOSTS:
        host = 'http://' + ALLOWED_HOSTS[0]
    else:
        host = 'http://localhost:8000'
    context = {'user': user, 'host': host,
               'sign': signer.sign(user.email)}
    subject = render_to_string('email/reset_password_subject.txt', context)
    body = render_to_string('email/reset_password_body.txt', context)
    user.email_user(subject, body)
