from django.db import models

# Create your models here.
class Query(models.Model):
	name = models.CharField(max_length=200)
	email = models.EmailField(null=False)
	body = models.TextField()
	phone = models.BigIntegerField(null=True,blank=True)
	created = models.DateTimeField(auto_now_add = True)
	prefered_reply = models.CharField(max_length=100,choices =(
		('Phone','Phone'),
		('Email','Email'),
		))
	class Meta:
		ordering = ("created",)
