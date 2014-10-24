# coding=utf8

from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

class Car(models.Model):
    user = models.ForeignKey(User, related_name="car")
    is_turnedon = models.BooleanField()
    is_locked = models.BooleanField()
    is_walking = models.BooleanField()
    play_alarm = models.BooleanField()
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __unicode__(self):
        """Display title as instance information"""
        return self.user.username
