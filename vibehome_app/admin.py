from django.contrib import admin
from .models import ContactMessage, Estate


@admin.register(Estate)
class EstateAdmin(admin.ModelAdmin):
    search_fields = ('offer_number', 'localization', 'property_type')
    list_display = ('offer_number', 'localization', 'property_type', 'price')

@admin.register(ContactMessage)
class ContactAdmin(admin.ModelAdmin):
    search_fields = ('name', 'phone', 'email')
    list_display = ('name', 'phone', 'email')
