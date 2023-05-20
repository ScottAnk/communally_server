from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie


def create(request):
    if request.method != "POST":
        return JsonResponse({"error": "invalid request type"})

    user = User.objects.create_user(
        request.POST["username"], request.POST["email"], request.POST["password"]
    )
    user.first_name = request.POST["first_name"]

    if "last_name" in request.POST and request.POST["last_name"] != "":
        user.last_name = request.POST.last_name
    user.save()
    return HttpResponse()
