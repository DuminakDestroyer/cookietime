from django.db import models
from django.utils import timezone

class Company(models.Model):
	company_name = models.CharField(max_length = 20)


class Employee(models.Model):
	account = models.ForeignKey('auth.User')
	date_started = models.DateTimeField(blank=False, null=False)
	shift_length = models.IntegerField(default=8)
	status_choices = (('R', 'Regular'), ('PT', 'Part Time'), ('P', 'Probationary'), ('I', 'Intern'), ('T', 'Terminated'), ('A', 'Admin'))
	status = models.CharField(max_length=2, choices = status_choices)

	def add_employee(self):
		self.date_started = timezone.now()
		self.save()

