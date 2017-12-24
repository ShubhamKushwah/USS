from django.db import models
from .utils import code_generator, create_shortcode

class ShortUrl(models.Model):
	url = models.CharField(max_length=220)
	shortcode = models.CharField(max_length=16, unique=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True)
	updated = models.DateTimeField(auto_now=True)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		super(ShortUrl, self).save(*args, **kwargs)
