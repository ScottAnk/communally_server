from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('<int:event_id>/', views.detail, name='event_detail'),
    path("create/", views.create,name='create_event')
]
