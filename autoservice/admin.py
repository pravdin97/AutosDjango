from django.contrib import admin

# Register your models here.

from autoservice.models import *

admin.site.register(Service)
admin.site.register(Offer)
admin.site.register(Autoservice)
