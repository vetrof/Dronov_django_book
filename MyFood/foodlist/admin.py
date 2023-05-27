from django.contrib import admin

from foodlist.models import Food, Type


class FoodAdminView(admin.ModelAdmin):
    list_display = ('name', 'info', 'type', 'id')
    ordering = ('-id',)


admin.site.register(Food, FoodAdminView)
admin.site.register(Type)
