from django.db import models

class Room(models.Model):
    name=models.CharField(max_length=1000)
    
    
class Message(models.Model):
    value= models.CharField(max_length=400000)
    time=models.TimeField(auto_now_add=True, blank=False)
    user=models.CharField(max_length=4000000)
    room=models.CharField(max_length=1000)