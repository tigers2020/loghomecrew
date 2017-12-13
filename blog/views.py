from braces.views import SelectRelatedMixin, LoginRequiredMixin
from django.shortcuts import render
from django.views import generic
from . import models


# Create your views here.


class BlogIndexView(generic.ListView, SelectRelatedMixin):
	model = models.BlogText
	select_related = ('themes', 'categories')


class BlogDetailView(generic.DetailView, SelectRelatedMixin):
	models = models.BlogText
	select_related = ('themes', 'categories')

	def get_queryset(self):
		queryset = super(BlogDetailView, self).get_queryset()
		return queryset.filter(
			blogtext_themes_ieact=self.kwargs.get('themes')
		)


class BlogWrite(LoginRequiredMixin, generic.TemplateView):
	template_name = "blog_write.html"
