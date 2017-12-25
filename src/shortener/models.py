from django.conf import settings
# from django.core.urlresolvers import reverse
from django.db import models
from django_hosts.resolvers import reverse
from .utils import code_generator, create_shortcode
from .validators import validate_url, validate_dot

SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 16)

class ShortURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs = super(ShortURLManager, self).all(*args, **kwargs)
		qs = qs.filter(active=True)
		return qs

	def refresh_shortcodes(self):
		qs = ShortUrl.objects.filter(id__gte=1)	# gte=greater than or equal to
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			q.save()
			new_codes += 1
		return "New Codes made {i}".format(i=new_codes)

class ShortUrl(models.Model):
	url = models.CharField(max_length=220, validators=[validate_url, validate_dot])
	shortcode = models.CharField(max_length=SHORTCODE_MAX, unique=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)
	active = models.BooleanField(default=True)

	objects = ShortURLManager()		# this is ShortUrl. -> objects <- .all()

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(ShortUrl, self).save(*args, **kwargs)

	def get_short_url(self):
		url_path = reverse("scode", kwargs={'shortcode': self.shortcode}, host='www', scheme='http')
		return url_path

