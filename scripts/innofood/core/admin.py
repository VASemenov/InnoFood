from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group

# admin.site.register(Manager)
admin.site.register(Cafe)
admin.site.register(Complaint)
admin.site.register(Order)
admin.site.unregister(Group)





