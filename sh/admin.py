from django.contrib import admin
from .models import *

class categoryadmin(admin.ModelAdmin):
    list_display=('name',)

class productadmin(admin.ModelAdmin):
    list_display=('name',)
    
admin.site.register(category,categoryadmin)
admin.site.register(product,productadmin)
# Register your models here.
