from django.db import models

class Uloha(models.Model):
    nazov = models.CharField(max_length=100)
    hotova = models.BooleanField(default=False)
    vytvorena = models.DateTimeField(auto_now_add=True)
    termin = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nazov