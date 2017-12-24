from django.db import models
from .utils import code_generator, create_shortcode

class ShortURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs = super(ShortURLManager, self).all(*args, **kwargs)
		qs = qs.filter(active=True)
		return qs

	def refresh_shortcodes(self):
		qs = ShortUrl.objects.filter(id_gte=1)	# gte=greater than or equal to
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			q.save()
			new_codes += 1
		return "New Codes made {i}".format(i=new_codes)

class ShortUrl(models.Model):
	url = models.CharField(max_length=220)
	shortcode = models.CharField(max_length=16, unique=True, blank=True)
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
