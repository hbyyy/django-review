from django.contrib import admin

# Register your models here.
from .models import TestUser


@admin.register(TestUser)
class TestUserAdmin(admin.ModelAdmin):
    pass

