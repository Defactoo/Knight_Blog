from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
	"""
	The category of blog
	"""
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Tag(models.Model):
	"""
	The tag of blog
	"""
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name

class Post(models.Model):
	"""
	The main model of blog
	"""
	#The title of blog
	title = models.CharField(max_length=70)

	#The body of blog
	body = models.TextField()

	#create time and modified time
	created_time = models.DateTimeField()
	modified_time = models.DateTimeField()

	#the degist of blog
	excerpt = models.CharField(max_length=200, blank=True)

	#the category and tags of blog,but the category attr was the foreign key of class Category
	category = models.ForeignKey(Category)
	#the tag attr was same with category but the relation between Post and Tag was many to many
	tags = models.ManyToManyField(Tag, blank=True)

	#author was a foreignkey of user
	author = models.ForeignKey(User)

	def __str__(self):
		return self.title
