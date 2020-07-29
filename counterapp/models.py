from django.db import models

class Counter(models.Model):
	number = models.CharField(max_length =10)

	def __str__(self):
		 return (self.number )
		
