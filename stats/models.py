from django.db import models


class Page(models.Model):
    url = models.URLField()
    nb_visites = models.IntegerField(default=1)

    def __str__(self):
        return self.url
