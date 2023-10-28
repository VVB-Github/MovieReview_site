from django.db import models

# Create your models here.


class News(models.Model):
    headlone = models.CharField(max_length=100)
    body = models.CharField(max_length=250)
    date = models.DateField()

    def __str__(self):
        return self.headlone
