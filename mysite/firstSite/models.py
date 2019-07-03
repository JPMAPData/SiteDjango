from django.db import models

class Suggest(models.Model):
    nome = models.CharField(max_length=15)
    url = models.URLField()
    def __str__(self):
        return self.nome

