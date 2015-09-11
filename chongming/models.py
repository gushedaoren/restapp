# coding=utf-8
from django.db import models
from django.contrib import admin
from django.db.models import ImageField
from tinymce.models import HTMLField
# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length=150, unique=True)
	created = models.DateTimeField(auto_now_add=True, auto_created=True)
	lastEditTime = models.DateTimeField(auto_now=True, auto_created=True)
	content = HTMLField()
	author = models.CharField(max_length=150)
	class Meta:
		abstract = True


class News(Article):
	newsSource=models.CharField(max_length=150)
	newsTime=models.DateTimeField()
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "新闻"
		verbose_name_plural = "新闻"

class Youji(Article):
	icon_url=models.CharField(max_length=1000, blank=True)
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "游记"
		verbose_name_plural = "游记"



class Nongjiale(Article):
	logo = ImageField(blank=True)
	img1 = ImageField(blank=True)
	img2 = ImageField(blank=True)
	img3 = ImageField(blank=True)
	img4 = ImageField(blank=True)
	img5 = ImageField(blank=True)
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "农家乐"
		verbose_name_plural = "农家乐"

admin.site.register(News)
admin.site.register(Youji)
admin.site.register(Nongjiale)