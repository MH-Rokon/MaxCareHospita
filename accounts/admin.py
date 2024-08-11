from django.contrib import admin
from .models import UserAddress,Category,UserAccount 

admin.site.register(UserAddress)
admin.site.register(Category)
admin.site.register(UserAccount)