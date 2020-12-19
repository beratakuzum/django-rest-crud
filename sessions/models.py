from django.db import models
from events.models import Event


class Session(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    start_date = models.DateTimeField(null=False, blank=False)
    end_date = models.DateTimeField(null=False, blank=False)
    speaker = models.CharField(max_length=100, null=False, blank=False)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)

    class Meta:
        ordering = ['start_date']

    def __str__(self):
        return "%s" % self.name
