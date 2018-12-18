from django.db import models
#import User model
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	team_name = models.CharField(max_length=50)
	student_name = models.CharField(max_length=50)
	member_name = models.CharField(max_length=50)
	member_name2 = models.CharField(max_length=50)
	college = models.TextField(max_length=150)
	phone = models.CharField(max_length=12)


	def __str__(self):
		return self.student_name

class Event(models.Model):
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to='event_image')
	topics = models.TextField(null=True,blank=True)
	max_part_stud = models.PositiveIntegerField(default=2)
	time = models.CharField(max_length=50)
	venue = models.CharField(max_length=20)
	rules = models.TextField()

	def __str__(self):
		return self.name
