from django.db import models
from django.utils import timezone

class reminder(models.Model):
    reminder_subject = models.CharField(max_length=200)
    reminder_message = models.TextField(max_length=2000)
    created_date = models.DateTimeField('date created')
    reminder_date = models.DateTimeField('Date Due')
    def __str__(self):
        return self.reminder_subject
