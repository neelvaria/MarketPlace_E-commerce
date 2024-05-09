from django.contrib import admin

# Register your models here.
from .models import *

class categories(admin.ModelAdmin):
    list_display = ["name"]
admin.site.register(category,categories)

class itemss(admin.ModelAdmin):
    list_display = ["category","name","description","price","image","is_sold","created_by","created_at"]
admin.site.register(item,itemss)