from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, null=True,
                             blank=True, default=None)
    trackingnumber = models.CharField(
        max_length=100, null=True, blank=True, default=None)
    sender = models.CharField(
        max_length=100, null=True, blank=True, default=None)
    receiver = models.CharField(
        max_length=100, null=True, blank=True, default=None)
    subject = models.CharField(
        max_length=100, null=True, blank=True, default=None)
    option_choices = [('outgoing', 'Outgoing'), ('incoming', 'Incoming')]
    option = models.CharField(
        max_length=100, choices=option_choices, default='outgoing')
    attachment = models.FileField(
        upload_to='attachment', null=True, blank=True, default=None)

    def __str__(self):
        return self.title
