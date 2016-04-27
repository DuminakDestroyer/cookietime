from django.contrib import admin
from .models import Company, Employee, Leave, Log, Offset, Notification, Message

admin.site.register(Company)
admin.site.register(Employee)
admin.site.register(Leave)
admin.site.register(Log)
admin.site.register(Offset)
admin.site.register(Notification)
admin.site.register(Message)