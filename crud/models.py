from django.db import models

class TodoModel (models.Model):
	task = models.CharField (max_length=20)

	def __str__(self):
		return self.task
