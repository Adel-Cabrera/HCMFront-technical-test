from django.db import models

# Create your models here.


class Workhours(models.Model):
    WEEKDAYS = (
        ('MO', 'Monday'),
        ('TU', 'Tuesday'),
        ('WE', 'Wednesday'),
        ('TH', 'Thursday'),
        ('FR', 'Friday'),
        ('SA', 'Saturday'),
        ('SU', 'Sunday')
    )

    name = models.CharField(max_length=50)
    code = models.CharField(max_length=2)

    day_start = models.CharField(u'From', max_length=2,
                                 choices=WEEKDAYS, default='MO')
    day_end = models.CharField(u'Up to', max_length=2,
                               choices=WEEKDAYS, default='FR')

    start = models.TimeField('Entry', default='09:00')
    end = models.TimeField('Finish', default='17:00')

    class Meta:
        verbose_name = 'Workhour'
        verbose_name_plural = 'Workhours'


def __str__(self):
    return self.name
