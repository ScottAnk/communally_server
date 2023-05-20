from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Event
from .models import Post
from django.core import serializers
from django.shortcuts import render, get_object_or_404
from django.views import View


def index(self,requests):
    event_list=Event.objects.all()
    json_data=serializers.serialize('json',event_list)
    return JsonResponse(json_data, safe=False)
    
def create(self,request):
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

def detail(self, request, event_id):
    event=get_object_or_404(Event, id=event_id)
    data = {
       'event_id': event.id,
       'name': event.name,
       'time': event.time.strftime('%Y-%m-%d %H:%M:%S'),
       'location': event.location,
       'host': event.host.username,
       'description': event.description,
       'capacity': event.capacity,
       'tags':event.tag
    }
    return JsonResponse(data)
    
