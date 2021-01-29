from django.utils.translation import gettext as _


class StatusRequest:

    SUBMITTED = "submitted"
    APPROVED = "approved"
    CANCELED = "canceled"
    REJECTED = "rejected"

    CHOICES = (
        (SUBMITTED, _("submitted")),
        (APPROVED, _("approved")),
        (CANCELED, _("canceled")),
        (REJECTED, _("rejected")),
    )
