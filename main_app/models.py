from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class WouldYouRather(models.Model):
    question = models.CharField(max_length=250)
    option_one = models.CharField(max_length=50)
    option_two = models.CharField(max_length=50)
    option_one_count = models.IntegerField(default=0)
    option_two_count = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'question_id': self.id})
