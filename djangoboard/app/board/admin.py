from django.contrib import admin

# Register your models here.
from .models import Board, Tag


@admin.register(Board)
class BoardAdmin(admin.ModelAdmin):
    pass


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
