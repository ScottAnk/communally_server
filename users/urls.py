from django.urls import path, include

from . import views

urlpatterns = [
    path("create/", views.create, name="create_user"),
    path("login/", views.user_login, name="login_user"),
]
