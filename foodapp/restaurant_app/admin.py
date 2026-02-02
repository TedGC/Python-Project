from django.contrib import admin
from .models import Item
# Register your models here.


class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('menu_name', 'status')
    list_filter = ('status',)
    search_fields = ('meal_menu', 'description')


admin.site.register(Item, MenuItemAdmin)

#python manage.py createsuperuser
