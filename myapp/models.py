from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

class HomeInfo(models.Model):
	tagline = models.CharField(max_length=256)
	example_email = models.EmailField()
	email_button = models.CharField(max_length=256)

class Banner(models.Model):
	image = models.URLField()
	title = models.TextField()

class Blurb(models.Model):
	title = models.CharField(max_length=256)
	content = models.TextField()
	link = models.CharField(max_length=256)
	link_text = models.CharField(max_length=256)