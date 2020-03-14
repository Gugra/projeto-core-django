from django.db import models
from django.urls import	reverse
# Create your models here.
class Product (models.Model):
	title 			=models.CharField(max_length=120)
	description		=models.TextField(blank=True,null=True,max_length=350)
	price			=models.DecimalField(decimal_places=2,max_digits=100000)
	summary         =models.TextField(blank=True,null=True,max_length=350)
	featured 		=models.BooleanField(default=False)
	"""docstring for Products"""
	def get_absolute_url(self):
		return reverse("product-detail",kwargs={"id":self.id})
		