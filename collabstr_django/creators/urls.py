from django.urls import path
from . import views

urlpatterns = [
    path("creator/", views.CreatorListCreateView.as_view(), name="creator_list_create"),
    path(
        "creator/<int:pk>/",
        views.CreatorRetrieveUpdateDeleteView.as_view(),
        name="creator_retrieve_update_delete",
    ),
    path(
        "creator/<int:creator_id>/content/",
        views.ContentListCreateView.as_view(),
        name="content_list_create",
    ),
    path(
        "creator/<int:creator_id>/content/<int:pk>/",
        views.ContentRetrieveUpdateDeleteView.as_view(),
        name="content_retrieve_update_delete",
    ),
]
