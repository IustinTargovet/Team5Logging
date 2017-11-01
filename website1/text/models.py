from django.db import models

class Log(models.Model):
    title = models.CharField(max_length = 50)
    category = models.CharField(max_length = 50)
    date = models.DateTimeField()

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
