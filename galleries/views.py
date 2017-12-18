from braces.views import SelectRelatedMixin
from django.db.models import Count, Max
from django.http import Http404
from django.shortcuts import render
from django.views import generic
from .models import BuildingImages, Location


class GalleriesIndexView(generic.ListView):
	model = BuildingImages

	def get_context_data(self,**kwargs):
		context = super(GalleriesIndexView, self).get_context_data(**kwargs)
		context['locations'] = Location.objects.all()

		print(context)
		return context
# def get_context_data(self, **kwargs):
# 	context = super(GalleriesIndexView, self).get_context_data(**kwargs)
#
#
# 	galleries_image = []
# 	galleries = models.BuildingImages.objects.all()
# 	context['locations'] = models.Location.objects.all().order_by('state')
#
# 	year_ids = galleries.values_list('date_build', flat=True).distinct()
# 	year_set = set()
# 	for y in year_ids:
# 		year_set.add(y.year)
# 	print(year_set)
# 	for year in year_set:
# 		for location in context['locations']:
# 			if galleries.get(location=location, date_build__year=year):
# 				galleries_image += galleries.get(location=location, date_build__year=year)
#
# 	context['images'] = galleries_image
# 	return context


class GalleriesDetailView(SelectRelatedMixin, generic.ListView):
	model = BuildingImages
	select_related = ('location',)

	def get_queryset(self, **kwargs):
		print(kwargs)
		try:
			images = BuildingImages.objects.filter(date_build__year=kwargs['year']).order_by('date_build')
			images = images.filter(location=kwargs['pk'])

		except BuildingImages.DoesNotExist:
			raise Http404
		else:
			print(images)
			return images.all()
	#
	# def get_context_data(self, **kwargs):
	# 	context = super().get_context_data(**kwargs)
	# 	context['images'] = self.location
	# 	return context
