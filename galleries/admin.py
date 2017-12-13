from django.contrib import admin
from django.utils.html import format_html

from . import models


# Register your models here.


def apply_to_front(modeladmin, request, queryset):
	for front_check in queryset:
		if front_check.front_view:
			front_check.front_view  = False
		else:
			front_check.front_view = True

		front_check.save()
	apply_to_front.short_description="enable to front view"

class GalleriesAdmin(admin.ModelAdmin):
	list_display = ("title", "front_view", "location", "date_build",)
	ordering = ('date_build',)
	actions = [apply_to_front,]


class LocationAdmin(admin.ModelAdmin):
	list_display = ('state', 'name')
	ordering = ('state',)


admin.site.register(models.BuildingImages, GalleriesAdmin)
admin.site.register(models.Location, LocationAdmin)
