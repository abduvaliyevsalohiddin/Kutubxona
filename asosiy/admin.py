from django.contrib import admin
from django.contrib.auth.models import Group, User

from .models import *


@admin.register(Muallif)
class MuallifAdmin(admin.ModelAdmin):
    list_display = ["id", "ism", "jins", "tugulgan_kun", "tirik", "kitoblar_soni"]
    list_display_links = ["id", "ism"]
    list_editable = ["tirik", "kitoblar_soni"]
    search_fields = ["id", "ism", "tugulgan_kun"]
    search_help_text = "Id , ism va tugulgan kun ustunlari bo'yicha qidiring"
    list_filter = ["tirik"]
    ordering = ["id"]
    date_hierarchy = "tugulgan_kun"
    list_per_page = 10


@admin.register(Kitob)
class KitobAdmin(admin.ModelAdmin):
    list_display = ["id", "nom", "sahifa", "janr", "muallif"]
    list_display_links = ["id", "nom"]
    search_fields = ["id", "nom", "muallif__ism"]
    search_help_text = "Id , nom va muallif ustunlari bo'yicha qidiring"
    list_filter = ["janr", "muallif"]
    list_editable = ["sahifa"]
    autocomplete_fields = ["muallif"]


admin.site.register(Talaba)
# admin.site.register(Muallif)
# admin.site.register(Kitob)
admin.site.register(Kutubxonachi)
admin.site.register(Record)

# admin.site.unregister(Group)
# admin.site.unregister(User)
