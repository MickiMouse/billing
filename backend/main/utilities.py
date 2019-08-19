from django.template.loader import render_to_string
from django.core.signing import Signer

signer = Signer()


def send_activation_notification(user):
    host = f'http://localhost:8080/login/{signer.sign(user.email)}'
    context = {'user': user, 'host': host}
    subject = render_to_string('email/activation_letter_subject.txt', context)
    body = render_to_string('email/activation_letter_body.txt', context)
    user.email_user(subject, body)


def send_request_reset_password(user):
    host = f'http://localhost:8080/password/{signer.sign(user.email)}'
    context = {'user': user, 'host': host,
               'sign': signer.sign(user.email)}
    subject = render_to_string('email/reset_password_subject.txt', context)
    body = render_to_string('email/reset_password_body.txt', context)
    user.email_user(subject, body)
