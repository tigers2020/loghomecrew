from django.shortcuts import render
from django.views import generic
from galleries.models import BuildingImages
from article.models import ArticleText
from article.models import Category


# Create your views here.
class IndexView(generic.TemplateView):
	template_name = 'home/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['buildImages'] = BuildingImages.objects.filter(front_view=True)
		context['articletext'] = ArticleText.objects.filter(category=1)
		context['aboutus'] = ArticleText.objects.get(title="About Us")
		return context
