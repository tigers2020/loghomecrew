from django.utils import timezone

from article.models import ArticleText
from . import models
from django.views import generic


# Create your views here.
class IndexView(generic.ListView):
	model = models.ArticleText


class ArticleList(generic.ListView):
	model = models.ArticleText


class Article(generic.DetailView):
	model = models.ArticleText
	template_name = 'article/article_detail.html'


class BlogView(generic.ListView):
	model = models.ArticleText.objects.filter(category=5)


class AboutUsView(generic.ListView):
	model = ArticleText
	template_name = 'article/about_us.html'

	def get_context_data(self, **kwargs):
		context = super(AboutUsView, self).get_context_data(**kwargs)
		context['about_us'] = ArticleText.objects.filter(category=2).order_by('pk')
		context['feed_back'] = ArticleText.objects.filter(category=3).order_by('pk')
		print(context)
		return context


class FaQView(generic.TemplateView):
	model = models.ArticleText
	template_name = 'article/faq.html'

	def get_context_data(self, **kwargs):
		context = super(FaQView, self).get_context_data(**kwargs)
		context['faqs'] = ArticleText.objects.filter(category=4)
		return context
