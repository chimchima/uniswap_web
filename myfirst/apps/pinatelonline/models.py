from django.db import models

class Swap(models.Model):
    token_in = models.CharField('token_in', max_length=228)
    token_out = models.CharField('token_out', max_length=228)
    amount_in = models.IntegerField('amount_in')
    amount_out = models.IntegerField('amount_out')
    objects = models.Manager()