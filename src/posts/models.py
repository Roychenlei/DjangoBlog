from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.core.urlresolvers import reverse

# Create your models here.

from django.utils.encoding import python_2_unicode_compatible
class Post(models.Model):
	title = models.CharField(max_length=120)
	content = models.TextField()
	updated = models.DateTimeField(auto_now=True,auto_now_add=False)
	timestamp = models.DateTimeField(auto_now=False,auto_now_add=True)
	def __unicode__(self):
		return self.title

	def __str__(self):
		return self.title
	def get_absolute_url(self):
		return reverse("posts:detail", kwargs={"id": self.id})


@python_2_unicode_compatible

class Comment(models.Model):
	post = models.ForeignKey(Post,on_delete=models.CASCADE)
	comment_text = models.CharField(max_length=200)

	def __str__(self):
		return self.comment_text