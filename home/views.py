from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views import generic
from galleries.models import BuildingImages
from article.models import ArticleText
from article.models import Category

from django.conf import settings
from django.core.mail import send_mail, mail_admins

# Create your views here.
from home.forms import ContactForm


class IndexView(generic.TemplateView):
	template_name = 'home/index.html'

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['buildImages'] = BuildingImages.objects.filter(category=1)
		context['articletext'] = ArticleText.objects.filter(category=1)
		context['aboutus'] = ArticleText.objects.get(title="About Us")
		return context


class ContactUsView(generic.TemplateView):
	template_name = 'home/contact_us.html'


def contact(request):
	form = ContactForm(request.POST or None)

	context = None
	errors = None
	if form.is_valid():
		print(form.cleaned_data)
		first_name = form.cleaned_data.get("first_name")
		last_name = form.cleaned_data.get("last_name")
		from_email = form.cleaned_data.get("email")
		subject = form.cleaned_data.get("subject") + "-" + first_name + " " + last_name
		body_message = form.cleaned_data.get("message")
		send_mail(subject, body_message, from_email, [settings.EMAIL_HOST_USER], fail_silently=False)
		mail_admins(subject, body_message, fail_silently=False)
		context['sent_email'] = "Sent Email Success"
		print("sent email")
		return HttpResponseRedirect("/")
	else:
		print("Form is not valid")
	context = {
		"form": form,
		'error': errors,
	}
	return render(request, "home/contact_us.html", context)


class TestView(generic.ListView):
	template_name = 'galleries/index.html'
	model = BuildingImages
