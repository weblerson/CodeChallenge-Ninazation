from django.db import models
from django.contrib.auth.models import User


class Avaliation(models.Model):

    choices = (
        ('P', 'Péssimo'),
        ('R', 'Ruim'),
        ('B', 'Bom'),
        ('E', 'Excelente')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    avaliation = models.CharField(max_length=15, choices=choices)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return '%s (%s): %s/%s' % (self.user.username, self.avaliation, self.date.day, self.date.month)


class Annotation(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    positive = models.TextField(max_length=500)
    negative = models.TextField(max_length=500)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return 'Anotações de %s em %s/%s' % (self.user.username, self.date.day, self.date.month)


class Crisis(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.BooleanField()
    start = models.TimeField()
    final = models.TimeField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return '%s sem crise' % self.user.username if not self.status else '%s: crise em %s/%s de %s até %s' \
                                                                            % (
                                                                                self.user.username,
                                                                                self.date.day,
                                                                                self.date.month,
                                                                                self.start,
                                                                                self.final
                                                                            )
