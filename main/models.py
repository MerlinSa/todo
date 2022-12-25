from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    text = models.CharField(max_length=100)
    persone = models.CharField(max_length=60)
    created_at = models.DateField(auto_now_add=True)
    phone_number = models.IntegerField()
    date_of_meeting = models.DateField()
    comment = models.CharField(max_length=100)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

