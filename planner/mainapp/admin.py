from django.contrib import admin
from .models import User, Task, Schedule

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Schedule)
