from django.contrib import admin
from .import models 
admin.site.register(models.availableTime)
admin.site.register(models.designation)
admin.site.register(models.specialization)
admin.site.register((models.doctor))
admin.site.register((models.review))

