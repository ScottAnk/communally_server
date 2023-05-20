from django.urls import path, include

from . import views

urlpatterns = [
    # creates endpoints /login/ /logout/ among others
    path("", include("django.contrib.auth.urls")),
    path("create/", views.create, name="create_user"),
]
