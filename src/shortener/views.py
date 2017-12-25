from django.http import HttpResponseRedirectfrom django.shortcuts import render, get_object_or_404from django.views import Viewfrom .forms import SubmitUrlFormfrom .models import ShortUrlfrom analytics.models import ClickEventclass HomeView(View):	def get(self, request, *args, **kwargs):		form = SubmitUrlForm()		context = {			"form": form,		}		return render(request, 'shortener/home.html', context)	def post(self, request, *args, **kwargs):		form = SubmitUrlForm(request.POST)		context = {			"form": form,		}		template = "shortener/home.html"		if form.is_valid():			url = form.cleaned_data.get('url')			obj, created = ShortUrl.objects.get_or_create(url=url)			context = {				'object': obj,				'created': created,			}			if created:				template = "shortener/success.html"			else:				template = "shortener/failure.html"		return render(request, template, context)class ShortRedirectView(View):	def get(self, request, shortcode=None, *args, **kwargs):		obj = get_object_or_404(ShortUrl, shortcode=shortcode)		ClickEvent.objects.create_event(obj)		return HttpResponseRedirect(obj.url)