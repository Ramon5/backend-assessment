from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def send_accepted_request_email_to_user(to, msg: str):
    subject = "Sua solicitação para débito automático foi aprovada!"
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, msg, from_email, [to])


def send_rejected_request_email_to_user(to, msg: str):
    subject = "Sua solicitação para débito automático foi rejeitada!"
    from_email = settings.DEFAULT_FROM_EMAIL
    send_mail(subject, msg, from_email, [to])
