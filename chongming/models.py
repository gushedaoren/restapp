# coding=utf-8
from django.core.urlresolvers import reverse

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

	class Meta:
		abstract = True


class News(Article):
	author = models.CharField(max_length=150)
	newsSource=models.CharField(max_length=150)
	newsTime=models.DateTimeField()
	def __unicode__(self):
		return self.title


	class Meta:
		verbose_name = "新闻"
		verbose_name_plural = "新闻"




class Youji(Article):
	summary = models.TextField(max_length=150)
	hot = models.IntegerField(default=0)
	author = models.CharField(max_length=150)
	icon_url = models.CharField(max_length=1000, blank=True)
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "游记"
		verbose_name_plural = "游记"



class Nongjiale(Article):
	summary = models.TextField(max_length=150)
	contact = models.CharField(max_length=150)
	phone = models.CharField(max_length=150)
	address = models.CharField(max_length=250)
	busRoutes = models.TextField(blank=True)
	carRoutes = models.TextField(blank=True)

	hot = models.IntegerField(default=0,verbose_name="热门")
	rank = models.IntegerField(default=0,verbose_name="推荐")
	logo = ImageField(blank=True)
	img1 = ImageField(blank=True)
	img2 = ImageField(blank=True)
	img3 = ImageField(blank=True)
	img4 = ImageField(blank=True)
	img5 = ImageField(blank=True)
	enable_comments = models.BooleanField(default=True)
	njlShow = models.CharField(max_length=1000,blank=True)
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "农家乐"
		verbose_name_plural = "农家乐"

class AD(Article):
	index = models.IntegerField(default=0)
	logo = ImageField(blank=True)
	img1 = ImageField(blank=True)
	img2 = ImageField(blank=True)
	img3 = ImageField(blank=True)
	img4 = ImageField(blank=True)
	img5 = ImageField(blank=True)
	link = models.CharField(max_length=150 , blank=True)

	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "广告"
		verbose_name_plural = "广告"

admin.site.register(News)
admin.site.register(Youji)
admin.site.register(Nongjiale)
admin.site.register(AD)