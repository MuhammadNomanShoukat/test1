from django.contrib import admin
from .models import Profile

""" here Profile model adding(register) to admin site"""
admin.site.register(Profile)