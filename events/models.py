from django.db import models
import pytz

TIMEZONES = tuple(zip(pytz.all_timezones, pytz.all_timezones))


# Create your models here.
class Event(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    time_zone = models.CharField(max_length=32, null=False, blank=False, choices=TIMEZONES)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return "%s" % self.name