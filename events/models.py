from django.db import models

from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Event(models.Model):
    name = models.CharField(max_length=100)
    time = models.DateTimeField()
    location = models.CharField(max_length=200)
    host = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    description = models.CharField(max_length=10000)
    capacity = models.IntegerField()
    attendees = models.ManyToManyField(
        User, related_name="events_attending"
    )  # reverse relationship
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.name[0:30]


class Post(models.Model):
    text = models.CharField(max_length=5000)
    votes = models.IntegerField(default=0)
    replies_to = models.ForeignKey(
        "self", on_delete=models.CASCADE, blank=True, null=True
    )
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[0:30]
