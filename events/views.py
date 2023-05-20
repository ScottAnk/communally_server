from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .models import Event, Post, Tag
from .models import Post
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.views import View

# from django.views.decorators.csrf import csrf_exempt


# @csrf_exempt
def event_index(request):
    event_list = Event.objects.all()
    json_data = serializers.serialize("json", event_list)
    return JsonResponse(json_data, safe=False)


# @csrf_exempt
@login_required
def create_event(request):
    if request.method == "POST":
        name = request.POST.get("name")
        time = request.POST.get("time")
        location = request.POST.get("location")
        capacity = request.POST.get("capacity")
        tags = request.POST.getlist("tag")
        host = User.objects.get(username=request.user.username)
        # host = request.user
        description = request.POST.get("description")

        # need to add host parameter to this once users are handled
        event = Event.objects.create(
            name=name,
            time=time,
            location=location,
            capacity=capacity,
            description=description,
            host=host,
        )
        event.tag.set(tags)
        return JsonResponse({"event_id": event.id})
    else:
        return JsonResponse({"error": "Invalid request method"})


# @csrf_exempt
def event_detail(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    tags = list(event.tag.values())
    data = {
        "event_id": event.id,
        "name": event.name,
        "time": event.time.strftime("%Y-%m-%d %H:%M:%S"),
        "location": event.location,
        "host": event.host.name,
        "description": event.description,
        "capacity": event.capacity,
        "tags": tags,
    }
    return JsonResponse(data)


# @csrf_exempt
def create_tag(request):
    if request.method == "POST":
        name = request.POST.get("name")

        tag = Tag.objects.create(name=name)
        return JsonResponse({"event_id": tag.id})
    else:
        return JsonResponse({"error": "Invalid request method"})


# Add_attendee() --> called when invite accepted, or going to an event.
# make_post(,event.id) --> replies(m),
