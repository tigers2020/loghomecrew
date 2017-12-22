from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views import generic
from galleries.models import BuildingImages
from article.models import ArticleText
from anymail.message import AnymailMessage
from django.conf import settings
from django.core.mail import send_mail, EmailMessage

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
	thank_you = {}
	if request.method == 'GET':
		form = ContactForm()
	else:
		form = ContactForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)
			first_name = form.cleaned_data.get("first_name")
			last_name = form.cleaned_data.get("last_name")
			from_email = form.cleaned_data.get("email")
			feedback = form.cleaned_data('feed_back')

			subject = '[%s]'.format(feedback) + form.cleaned_data.get("subject") + "-" + first_name + " " + last_name
			body_message = form.cleaned_data.get("message")

			if send_mail(subject, body_message, from_email, recipient_list=['paulnephesh@gmail.com'],
						 html_message=body_message):
				print("sending email success")
				thank_you = {"You have successfully submitted. We will contact you in short time."}
			else:
				print('sending email failed')

	return render(request, "home/contact_us.html", {'form': form, 'success': thank_you})


def contact_success(request):
	return HttpResponse("Success! Thank you for your message")


def contact_failed(request):
	return HttpResponse("Send Email Failed")
