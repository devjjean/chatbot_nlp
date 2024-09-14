from django.contrib import admin
from .models import ExampleModel

@admin.register(ExampleModel)
class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ('name',)