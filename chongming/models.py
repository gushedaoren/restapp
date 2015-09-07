from django.db import models
from django.contrib import admin
from tinymce.models import HTMLField
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=150)
	created = models.DateTimeField()
	lastEditTime = models.DateTimeField()
	content = HTMLField()
	author = models.CharField(max_length=150)
	class Meta:
		abstract = True


class News(Article):
	newsSource=models.CharField(max_length=150)
	newsTime=models.DateTimeField()


admin.site.register(News)