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

	def get_absolute_url(self):
    		 return reverse('chongming.views.news_detial', args=[str(self.id)])


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
	def get_absolute_url(self):
    		 return reverse('chongming.views.travel_detial', args=[str(self.id)])
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


	def get_absolute_url(self):
    		 return reverse('chongming.views.nongjiale_detial', args=[str(self.id)])
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

class Shanghu(models.Model):
	title = models.CharField(max_length=150, unique=True)
	contact = models.CharField(max_length=150, blank=True)
	phone = models.CharField(max_length=150)
	address = models.CharField(max_length=250, blank=True)
	remark = HTMLField(blank=True)
	status=models.IntegerField(default=0)
	def __unicode__(self):
		return self.title
	class Meta:
		verbose_name = "商户通讯录"
		verbose_name_plural = "商户通讯录"

class ShanghuAdmin(admin.ModelAdmin):
    list_display = ('title','address','phone')

class Food(Article):
	summary = models.TextField(max_length=150)

	author = models.CharField(max_length=150)
	icon_url = models.CharField(max_length=1000, blank=True)
	def __unicode__(self):
			return self.title
	def get_absolute_url(self):
    		 return reverse('chongming.views.travel_detial', args=[str(self.id)])
	class Meta:
		verbose_name = "美食"
		verbose_name_plural = "美食"

class Health(Article):
	summary = models.TextField(max_length=150)

	author = models.CharField(max_length=150)
	icon_url = models.CharField(max_length=1000, blank=True)
	def __unicode__(self):
			return self.title
	def get_absolute_url(self):
    		 return reverse('chongming.views.health_detial', args=[str(self.id)])
	class Meta:
		verbose_name = "健康"
		verbose_name_plural = "健康"

admin.site.register(News)
admin.site.register(Youji)
admin.site.register(Nongjiale)
admin.site.register(AD)
admin.site.register(Shanghu,ShanghuAdmin)
admin.site.register(Food)
admin.site.register(Health)