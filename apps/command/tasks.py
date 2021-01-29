from __future__ import absolute_import, unicode_literals

from celery import shared_task

from apps.mail import (
    send_accepted_request_email_to_user,
    send_rejected_request_email_to_user,
)


@shared_task
def approve_request(email):
    try:
        send_accepted_request_email_to_user(
            email, "Parabéns! Sua solicitação foi aprovada."
        )
        return "email sended successfully"
    except Exception as e:
        return f"FAILURE: {e}"


@shared_task
def reject_request(email):
    try:
        send_rejected_request_email_to_user(
            email, "Eu sinto muito, mas sua solicitação foi recusada!"
        )
        return "email sended successfully"
    except Exception as e:
        return f"FAILURE: {e}"
