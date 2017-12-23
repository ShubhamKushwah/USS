from django.db import models


class ShortUrl(models.Model):
	url = models.CharField(max_length=220)
	shortcode = models.CharField(max_length=16, unique=True)

	def __str__(self):
		return str(self.url)

	def __unicode__(self):
		return str(self.url)
