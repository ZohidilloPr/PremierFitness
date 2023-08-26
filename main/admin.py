from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import (Treiner, Weeks, Times, Contact, Member)
# Register your models here.

@admin.action(description="Duplicate")
def duplicate(modeladmin, request, queryset):
    for i in queryset:
        i.pk = None
        i.save()


@admin.register(Treiner)
class TrainerAdmin(admin.ModelAdmin):
    list_filter = ("add_time", )
    readonly_fields = ("preview",)
    list_editable = ("order_num", )
    list_display_links = ("f_name", )
    list_display = ("id", "f_name", "professional", "order_num", "add_time")


    fieldsets = (
        ("Umumiy Malumotlar", {
            "fields": (
                ("f_name_uz", "f_name_ru", "f_name_en"), 
                ("professional_uz", "professional_ru", "professional_en"), 
                "order_num", 
            ),
        }),
        ("Xaqida", {
            "fields": (
               "about_uz", "about_ru", "about_en"
            ),
        }),
        ("URLs", {
            "fields": (
                "instagram", "facebook", "telegram",
            ),
        }),
        ("Foto", {
            "fields": (
                "img", "preview"
            ),
        })
    )


    def preview(self, obj):
        return mark_safe(f"<img src='{obj.img.url}' width='400'>")
    preview.short_description = "Trainer Foto"


@admin.register(Times)
class TimesAdmin(admin.ModelAdmin):
    list_display = ("id", "come_time", "left_time")


@admin.register(Weeks)
class WeeksAdmin(admin.ModelAdmin):
    actions = (duplicate, )
    list_display = ("name_uz", )
    filter_horizontal = ("time", )
    fields = ("author", "name_uz", "name_ru", "name_en", "time")

    def save_model(self, request, obj, form, change):
        obj.author = request.user
        return super().save_model(request, obj, form, change)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    ordering = ("-add_time", )
    list_display_links = ("f_name", )
    search_fields = ("f_name", "phone")
    list_filter = ("add_time", "update_time")
    list_display = ("id", "f_name", "phone", "text", "add_time", "update_time")


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    ordering = ("-add_time", )
    list_display_links = ("f_name", )
    search_fields = ("f_name", "phone")
    list_filter = ("add_time", "update_time")
    list_display = ("id", "f_name", "phone", "text", "add_time", "update_time")

