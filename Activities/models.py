from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class task(models.Model):
    content=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date_posted=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

    def get_absolute_url(self):
        return reverse('detail-task',kwargs={'username':self.author.username,'pk':self.pk})