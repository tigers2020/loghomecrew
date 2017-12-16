from django.db import models
from PIL import Image
from PIL.ExifTags import TAGS
from django.urls import reverse
from django_resized import ResizedImageField


# Create your models here.
class Location(models.Model):
	state = models.CharField(max_length=2)
	latitude = models.FloatField()
	longitude = models.FloatField()
	name = models.CharField(max_length=32)

	def __str__(self):
		return '[' + self.state + ']' + self.name

	class Meta:
		ordering = ["-name"]


def image_folder(instance, filename):
	return '/'.join([instance.location.state, str(instance.date_build.year), str(instance.date_build.month), filename])


class BuildingImages(models.Model):
	title = models.CharField(max_length=255)
	front_view = models.BooleanField(default=False)
	location = models.ForeignKey(Location, on_delete=models.CASCADE)
	date_build = models.DateField(auto_created=False, auto_now=False, auto_now_add=False, blank=True)
	image = ResizedImageField(null=True, blank=True, upload_to=image_folder, size=[1280, 720], keep_meta=True,
							  quality=90)
	description = models.TextField()

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):

		Image.open(self.image)
		info = Image.Image.info

	class Meta:
		ordering = ['-date_build']
