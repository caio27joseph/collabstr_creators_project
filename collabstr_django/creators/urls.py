from django.urls import path

from . import views
from . import api_views

urlpatterns = [
    path("api/creator/", api_views.CreatorListCreateAPIView.as_view(), name="creator_list_create"),
    path(
        "api/creator/<int:pk>/",
        api_views.CreatorRetrieveUpdateDeleteAPIView.as_view(),
        name="creator_retrieve_update_delete",
    ),
    path(
        "api/creator/<int:creator_id>/content/",
        api_views.ContentListCreateAPIView.as_view(),
        name="content_list_create",
    ),
    path(
        "api/creator/<int:creator_id>/content/<int:pk>/",
        api_views.ContentRetrieveUpdateDeleteAPIView.as_view(),
        name="content_retrieve_update_delete",
    ),
    path("creators/", views.creator_list_view, name="creator_list"),
]
