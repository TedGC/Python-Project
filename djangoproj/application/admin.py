from django.contrib import admin
from .models import Form



class FormAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'occupation', 'date')
    search_fileds = ('first_name', 'last_name', 'email', 'occupation', 'date')
    list_filter = ('first_name', 'last_name', 'email', 'occupation', 'date')
    readonly_fields = ('occupation', )
    
    
    # search_fields = ['first_name', 'last_name', 'email', 'occupation', 'date']
    # list_filter = ['occupation']
    # @admin.display(empty)

admin.site.register(Form, FormAdmin)


