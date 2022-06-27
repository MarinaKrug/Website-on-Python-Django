from django.contrib import admin

from locks.models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('cat', 'slug')
    prepopulated_fields = {'slug': ('cat',)}


class SalesAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'photo', 'time_create', 'time_update', 'is_published', 'cat')
    list_editable = ('is_published',)
    list_filter = ('time_create', 'cat', 'is_published')


class PriceAdmin(admin.ModelAdmin):
    list_display = ('cat', 'price')


class GalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'cat', 'photo')

class ContactsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone_number', 'date', 'time', 'message')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Price, PriceAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Contacts, ContactsAdmin)
