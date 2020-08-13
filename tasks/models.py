from django.db import models
from django.urls import reverse


class Task(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField(blank=True)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse('detail_task', args=[str(self.id)])