from django.contrib import admin
from .models import Receipe

# Register your models here.

@admin.register(Receipe)
class ReceipeAdmin(admin.ModelAdmin):
    list_display = ['id', 're_name', 're_description', 're_price', 're_images']