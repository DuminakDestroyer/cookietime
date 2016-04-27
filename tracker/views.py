from django.shortcuts import render, get_object_or_404
from .models import Company, Employee, Log, Message
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core import serializers
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils.timezone import utc
import datetime
import json
import time


@login_required
def home(request):
	if request.POST:
		message = request.POST.get('message')
		ltype = request.POST.get('type')
		user = request.user
		employee = get_object_or_404(Employee, account=user)
		if(ltype =='O'):
			log = Log.objects.get(employee=employee, end=None)
			log.end = timezone.now()
			log.end_message = message
			log.save()
		else:
			Log.objects.create(employee=employee, start=timezone.now(), start_message=message)
		return redirect("https://cookietime.herokuapp.com/")
	company = Company.objects.all()
	user = request.user
	employee = get_object_or_404(Employee, account=user)
	logs = Log.objects.all().filter(employee = employee).order_by('-start')
	if not logs:
		show= 'S'
	else:
		latest = logs[0].start
		if latest.date() <=timezone.now().date() and logs[0].end is not None:
			show = 'N'
		else:
			show = 'S'
	shift = employee.shift_length
	if not logs:
			log_type = 'O'
			seconds = 0
	else:
		if logs[0].end is None:
			log_type = 'I'
			timer= logs[0].start
		else:
			log_type = 'O'
			timer= logs[0].start
		end = timer + timedelta(hours=shift)
		now = timezone.now()
		timediff = end - now
		seconds =  timediff.total_seconds()
	return render(request, 'tracker/home.html', {'user': user, 'company': company, 'employee' : employee,  'logs' : logs, "type" : log_type, "shift" : shift, 'seconds' : seconds, 'show': show})

@login_required
def logs(request):
	user = request.user
	company = Company.objects.all()
	employee = get_object_or_404(Employee, account=user)
	logs = Log.objects.all().filter(employee = employee).order_by('-start')
	return render(request, 'tracker/logs.html', {'user': user, 'employee' : employee,'company': company, 'logs':logs})

@login_required
def messages(request):
	employees = Employee.objects.all()
	users = []
	for employee in employees:
		user = employee.account
		user_name = user.first_name+" "+user.last_name
		last_log = Log.objects.all().filter(employee = employee).order_by('-start')
		if not last_log:
			print("Empty")
		else:
			if last_log[0].end is None:
				text = last_log[0].start_message
				time = last_log[0].start
				actual_time = (time+ timedelta(hours=8)).strftime("%Y-%m-%d %I:%M %p") 
			else:
				text = last_log[0].end_message
				time = last_log[0].end
				actual_time = (time+ timedelta(hours=8)).strftime("%Y-%m-%d %I:%M %p") 
			user = Message(message_id=employee.pk, author=user_name, text=text, time=actual_time)
			users.append(user)
	users.sort(key=lambda x: x.time, reverse=True)
	results = [ob.as_json() for ob in users]
	return HttpResponse(json.dumps(results), content_type="application/json")


