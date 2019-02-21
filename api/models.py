from django.db import models


class Ubicacion(models.Model):
    fecha = models.DateTimeField(auto_now_add=True)
    lat = models.FloatField(max_length=255, blank=True, unique=False, null=True)
    lng = models.FloatField(max_length=255, blank=True, unique=False, null=True)

    def __str__(self):
        return "{}".format(self.fecha, self.lat, self.lng)
