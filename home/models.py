
from django.db import models

# Create your models here.

class Home(models.Model):
  banner = models.ImageField(upload_to = 'banner')
  logo = models.ImageField(upload_to = 'logo',default='logo.png')
class About(models.Model):
  title = models.CharField(max_length = 100)
  sub_title = models.CharField(max_length = 255)
  description_1 = models.TextField()
  description_2 = models.TextField(default = 'hellohello')
  banner = models.ImageField(upload_to = 'banner',default = 'media/banner/comment.jpg')

class Hobbies(models.Model):
  hobbie_title = models.CharField(max_length = 50)
  icon_class_1 = models.CharField(max_length = 50)
  icon_class_2 = models.CharField(max_length = 50)
  def __str__(self):
    return self.hobbie_title
class What_I_Do(models.Model):
  title = models.CharField(max_length = 100)
  description = models.TextField()
  icon_class_1 = models.CharField(max_length = 50)
  icon_class_2 = models.CharField(max_length = 50)
  def __str__(self):
    return self.title

class Expertise_caption(models.Model):
  caption = models.TextField()
  def __str__(self):
    return 'caption'

class Expertise_item(models.Model):
  title = models.CharField(max_length = 100)
  percentage = models.IntegerField()
  def __str__(self):
    return self.title

class Comment(models.Model):
  first_name = models.CharField(max_length = 50)
  second_name = models.CharField(max_length = 50)
  comment = models.TextField()
  profile = models.ImageField(upload_to = 'profiles')
  def __str__(self):
    return self.second_name

class Contact_Info(models.Model):
  title = models.CharField(max_length = 100)
  caption = models.TextField()
  info = models.TextField(default = 'kavappura')
  icon_class_1 = models.CharField(max_length = 50)
  icon_class_2 = models.CharField(max_length = 50)
  def __str__(self):
    return self.title

class Footer(models.Model):
  footer_logo = models.ImageField(upload_to = 'logo',default = 'logo.png')
  footer_caption = models.TextField()

class Footer_link(models.Model):
  name = models.CharField(max_length = 100)
  icon_class_1 = models.CharField(max_length = 50)
  icon_class_2 = models.CharField(max_length = 50)
  link = models.TextField(default = 'www.google.com')
  def __str__(self):
    return self.name

class Copyright(models.Model):
  owner = models.CharField(max_length = 255)
  developer = models.CharField(max_length = 255)
  year = models.CharField(max_length = 4)
  def __str__(self):
    return self.owner
  
  
