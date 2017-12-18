from braces.views import SelectRelatedMixin
from django.db.models import Count, Max
from django.http import Http404
from django.shortcuts import render
from django.views import generic
from . import models


# Create your views here.
def get_image_count_from_location(request):
	images = models.BuildingImages.objects.filter(request.state).count()
	return images


class GalleriesIndexView(generic.TemplateView):
	template_name = 'galleries/index.html'

	def get_context_data(self, **kwargs):
		context = super(GalleriesIndexView, self).get_context_data(**kwargs)
		context['locations'] = models.Location.objects.all().order_by('state')
		galleries_image = []
		galleries = models.BuildingImages.objects.all()
		year_ids = galleries.values_list('date_build', flat=True).distinct()
		year_set = set()
		for y in year_ids:
			year_set.add(y.year)

		print(year_set)
		for year in year_set:
			for location in context['locations']:
				galleries_image.append(models.BuildingImages.objects.get(location=location, date_build__year=year))

		context['images'] = galleries_image
		return context

	def get_image_by_year(self):
		pass


class GalleriesDetailView(SelectRelatedMixin, generic.ListView):
	model = models.BuildingImages
	select_related = ('location',)

	def get_queryset(self):
		print(self.kwargs)
		try:
			images = models.BuildingImages.objects.filter(date_build__year=self.kwargs['year']).order_by('date_build')
			images = images.filter(location=self.kwargs['pk'])

		except models.BuildingImages.DoesNotExist:
			raise Http404
		else:
			print(images)
			return images.all()


def get_context_data(self, **kwargs):
	context = super().get_context_data(**kwargs)
	context['images'] = self.location
	return context
