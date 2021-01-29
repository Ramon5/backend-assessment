from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext as _

from .constants import StatusRequest


class ActivationRequest(models.Model):

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(_("created at"), auto_now=True)
    status = models.CharField(
        _("status"),
        max_length=9,
        choices=StatusRequest.CHOICES,
        default=StatusRequest.SUBMITTED,
    )

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.owner.first_name} {self.owner.last_name}"
