from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.utils.text import slugify
import misaka
from taggit.managers import TaggableManager

# Create your models here.
from django.utils import timezone

User = get_user_model()


class BlogCategory(models.Model):
	theme = models.ForeignKey(BlogTheme, on_delete=models.CASCADE)
	category_name = models.CharField(max_length=255)

	def __str__(self):
		return self.category_name

class BlogTheme(models.Model):
	theme_name = models.CharField(max_length=255)


class BlogText(models.Model):
	title = models.CharField(max_length=255)
	category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, blank=True, null=True, related_name='categories')
	theme = models.ForeignKey(BlogTheme, on_delete=models.CASCADE, related_name='themes')
	tags = TaggableManager()
	slug = models.SlugField(unique=True, allow_unicode=True)
	publish = models.BooleanField(default=False)
	publish_date = models.DateTimeField(blank=True, null=True)
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now_add=True)
	blog_text = models.TextField(blank=True, default='')
	blog_text_html = models.TextField(editable=False, default="", blank=True)
	ip = models.IPAddressField()


	def publish(self):
		self.publish_date = timezone.now()
		self.save()

	def save(self, *args, **kwargs):
		self.modified_date = timezone.now()
		self.slug = slugify(self.title)
		self.blog_text_html = misaka.html(self.blog_text)
		super(BlogText, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('detail')
	def __str__(self):
		return self.title

	class Meta:
		verbose_name = "Entry"
		verbose_name_plural = "Entries"
		ordering = ["-created_date"]


class BlogComments (models.Model):

	user = models.ForeignKey(User, related_name='blog')
	blog_article_id = models.ForeignKey(BlogText, on_delete=models.CASCADE)
	comment = models.TextField()
	created_date = models.DateTimeField(auto_now_add=)
	ip = models.IPAddressField()
	


