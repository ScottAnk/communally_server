from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Event, User, Post, Tag
from .models import Post
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.views import View


def event_index(request):
    event_list=Event.objects.all()
    json_data=serializers.serialize('json',event_list)
    return JsonResponse(json_data, safe=False)
    
def create_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        time = request.POST.get('time')
        location = request.POST.get('location')
        capacity = request.POST.get('capacity')
        tag = request.POST.get('tag')
  
        event = Event.objects.create(name=name, time=time, location=location,capacity=capacity,
                                    tag=tag)
        return JsonResponse({'event_id': event.id})
    else:
            return JsonResponse({'error': 'Invalid request method'})

def event_detail(request, event_id):
    event=get_object_or_404(Event, id=event_id)
    tags= list(event.tag.values())
    data = {
       'event_id': event.id,
       'name': event.name,
       'time': event.time.strftime('%Y-%m-%d %H:%M:%S'),
       'location': event.location,
       'host': event.host.name,
       'description': event.description,
       'capacity': event.capacity,
       'tags':tags
    }
    return JsonResponse(data)

def register_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
  
        user = User.objects.create(name=name, email=email)
        return JsonResponse({'event_id': user.id})
    else:
            return JsonResponse({'error': 'Invalid request method'})

def create_tag(request):
    if request.method == 'POST':
        name = request.POST.get('name')
  
        user = Tag.objects.create(name=name)
        return JsonResponse({'event_id': user.id})
    else:
            return JsonResponse({'error': 'Invalid request method'})
    
