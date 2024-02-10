from django.contrib import admin
from .models import Items


class MenuItemListAdmin(admin.ModelAdmin):
    list_display = ('meal', 'price',)


admin.site.register(Items, MenuItemListAdmin)