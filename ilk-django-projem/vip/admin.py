from django.contrib import admin
from vip.models import  Subscribe
# Register your models here.



class SubscribeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'type']
    list_filter = ['type']
    search_fields= ['user__username']


admin.site.register(Subscribe, SubscribeAdmin)