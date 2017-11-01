from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import Permission, User

class Log(models.Model):
    user = models.ForeignKey(User, default=1)
    title = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50)
    date = models.DateTimeField()
    is_favorite = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('text:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class Entry(models.Model):
    log = models.ForeignKey(Log, on_delete=models.CASCADE)
    title = models.CharField(max_length = 50)
    text = models.CharField(max_length = 500)
    date = models.DateTimeField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.title

# Create your models here.
