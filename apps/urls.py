from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.account.views import RegisterView, UserView
from apps.command.views import (
    CommandRequestApproveView,
    CommandRequestCancellingView,
    CommandRequestRejectView,
    CommandSubmitRequestView,
)
from apps.query.views import QueryActivationRequestsDetail, QueryActivationRequestsView

urlpatterns = []

account_urls = [
    path("api/login", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/token/refresh", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/register", RegisterView.as_view(), name="register"),
    path("api/users", UserView.as_view(), name="users"),
]

command_urls = [
    path(
        "api/submit_request",
        CommandSubmitRequestView.as_view(),
        name="api-submit-request",
    ),
    path(
        "api/approve_request/<int:id>",
        CommandRequestApproveView.as_view(),
        name="api-approve-request",
    ),
    path(
        "api/reject_request/<int:id>",
        CommandRequestRejectView.as_view(),
        name="api-reject-view",
    ),
    path(
        "api/cancelling_request/<int:id>",
        CommandRequestCancellingView.as_view(),
        name="api-cancelling-request",
    ),
]

query_urls = [
    path("api/requests", QueryActivationRequestsView.as_view(), name="requests"),
    path(
        "api/requests/<int:id>",
        QueryActivationRequestsDetail.as_view(),
        name="retrieve-request",
    ),
]

urlpatterns += account_urls + command_urls + query_urls
