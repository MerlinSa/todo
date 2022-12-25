from django.db import models


class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    text = models.CharField(max_length=100)
    persone = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField("Phone", max_length=20)
    date_of_meeting = models.CharField(blank=True, max_length=10)
    comment = models.CharField(max_length=100)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Habits(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    done_for_today = models.BooleanField(default=False)
    important = models.BooleanField(default=False)
    comment = models.CharField(max_length=100)