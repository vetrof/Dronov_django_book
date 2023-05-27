from django.contrib import admin
from bboard.models import Bd, Rubric


class BdAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published', 'rubric', 'id')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content')
    ordering = ('-id',)


admin.site.register(Bd, BdAdmin)
admin.site.register(Rubric)
