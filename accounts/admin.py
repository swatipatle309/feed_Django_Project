from django.contrib import admin
from .models import user

@admin.register(user)
class userAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'address')
    search_fields = ('first_name', 'last_name') 
# Register your models here.
