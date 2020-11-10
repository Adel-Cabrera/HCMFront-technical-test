from django.db import models

# Create your models here.


class Workhours(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Workhour'
        verbose_name_plural = 'Workhours'


def __str__(self):
    return self.name
