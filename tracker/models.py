from django.db import models
from django.utils import timezone
from django.utils import formats


class Company(models.Model):
	company_name = models.CharField(max_length = 20)
	company_link = models.CharField(max_length = 20)

	def __str__(self):
		return self.company_name


class Employee(models.Model):
	account = models.ForeignKey('auth.User')
	date_started = models.DateTimeField(blank=False, null=False)
	shift_length = models.IntegerField(default=8)
	status_choices = (('R', 'Regular'), ('PT', 'Part Time'), ('P', 'Probationary'), ('I', 'Intern'), ('T', 'Terminated'), ('A', 'Admin'))
	status = models.CharField(max_length=2, choices = status_choices)

	def __str__(self):
		return self.account.first_name +" "+ self.account.last_name

class Leave(models.Model):
	employee = models.ForeignKey('tracker.Employee', related_name = 'leaves')
	leave_choices = (('EL', 'Emergency Leave'), ('SL', 'Sick Leave'), ('VL', 'Vacation Leave'))
	type = models.CharField(max_length=2, choices = leave_choices)
	reason = models.TextField()
	date_filed = models.DateTimeField(default=timezone.now)
	date_filed_for = models.DateTimeField(null=False)
	date_reviewed = models.DateTimeField(default=timezone.now, null = True, blank = True)
	status_choices = (('A', 'Approved'), ('R', 'Rejected'), ('P', 'Pending'))
	status = models.CharField(max_length=1, choices=status_choices)

	def __str__(self):
		return self.status+ " : "+self.employee.account.first_name +" "+ self.employee.account.last_name +" - "+ self.type + " - FOR: "+str(self.date_filed_for)

class Log(models.Model):
	employee = models.ForeignKey('tracker.Employee', related_name='logs')
	start = models.DateTimeField(default=timezone.now)
	end = models.DateTimeField(null = True, blank = True)
	start_message = models.CharField(max_length=140)
	end_message = models.CharField(max_length=140, null = True, blank = True)


	def __str__(self):
		return self.employee.account.first_name+" "+ self.employee.account.last_name +" - " +str(self.start)+" "+str(self.end)

class Offset(models.Model):
	employee = models.ForeignKey('tracker.Employee', related_name='offsets')
	time_started = models.DateTimeField(default=timezone.now)
	time_ended = models.DateTimeField(null=True, default=timezone.now)
	date_applied = models.DateTimeField(null=False)
	status_choices = (('A', 'Approved'), ('R', 'Rejected'), ('P', 'Pending'))
	status = models.CharField(max_length=1, choices=status_choices)
	
	def __str__(self):
		return self.employee.account.first_name+" "+ self.employee.account.last_name +" - FOR:  "+str(self.date_applied)

class Notification(models.Model):
	viewer=models.ForeignKey('tracker.Employee')
	seen = models.BooleanField(default=False)
	message = models.TextField()

class Message(models.Model):
	message_id = models.IntegerField()
	author = models.CharField(max_length=140, null = True, blank = True)
	text = models.CharField(max_length=140, null = True, blank = True)
	time = models.CharField(max_length=140, null = True, blank = True)

	def as_json(self):
		return dict(
			id=self.message_id,
			author=self.author, 
			text=self.text,
			time=self.time)