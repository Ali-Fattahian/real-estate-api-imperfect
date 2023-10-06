from django.urls import path

from .views import (
    AgentListAPIView,
    ProfileDetailAPIView,
    TopAgentListAPIView,
    ProfileUpdateAPIView,
)

urlpatterns = [
    path("me/", ProfileDetailAPIView.as_view(), name="get_profile"),
    path(
        "update/<str:username>/", ProfileUpdateAPIView.as_view(), name="update_profile"
    ),
    path("agents/all/", AgentListAPIView.as_view(), name="all-agents"),
    path("top-agents/all/", TopAgentListAPIView.as_view(), name="top-agents"),
]
