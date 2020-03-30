from django.db import models
from django.contrib.postgres.fields import JSONField

class OriginalSmartphone(models.Model):
    data = JSONField()
    append_datetime = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.data["DeviceName"]

    class Meta:
        app_label = "api"

class ScrapedSmartphone(models.Model):
    site = models.CharField(max_length = 200)
    data = JSONField()
    append_datetime = models.DateTimeField(auto_now = True)
    class Meta:
        app_label = "api"

    def __str__(self):
        return self.data["name"] + "  -  " + self.site


class OriginalLaptop(models.Model):
    data = JSONField()
    append_datetime= models.DateTimeField(auto_now = True)

    class Meta:
        app_label = "api"

    def __str__(self):
        return self.data['result']['0']['model_info'][0]['name']

class ScrapedLaptop(models.Model):
    site = models.CharField(max_length = 200)
    data = JSONField()
    append_datetime = models.DateTimeField(auto_now = True)
    searched = models.BooleanField(default = False)
    class Meta:
        app_label = "api"

    def __str__(self):
        return self.data["name"] + "  -  " + self.site

