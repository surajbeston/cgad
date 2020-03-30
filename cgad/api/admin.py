from django.contrib import admin
from .models import OriginalSmartphone, OriginalLaptop, ScrapedSmartphone, ScrapedLaptop

admin.site.register(OriginalSmartphone)

admin.site.register(ScrapedSmartphone)

admin.site.register(OriginalLaptop)

admin.site.register(ScrapedLaptop)
