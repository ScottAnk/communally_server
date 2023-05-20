from django.urls import path

from . import views

urlpatterns = [
    path("", views.event_index, name="index"),
    path("<int:event_id>/", views.event_detail, name="event_detail"),
    path("create_event/", views.create_event, name="create_event"),
    path("create_tag/", views.create_tag, name="create_tag"),
]
