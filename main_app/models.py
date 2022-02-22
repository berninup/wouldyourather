from django.db import models

class WouldYouRather(models.Model):
    question = models.CharField(max_length=250)

class Choice(models.Model):
    choice = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(WouldYouRather, on_delete=models.CASCADE)
