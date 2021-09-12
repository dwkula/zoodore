from django.contrib import admin
from .models import Announcement
# Register your models here.


class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('author', 'title', 'slug', 'creation_date', 'city')


admin.site.register(Announcement, AnnouncementAdmin)
