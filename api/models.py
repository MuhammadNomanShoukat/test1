from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.admin import User


# =========================================== Profile model creating here ======================================
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,default="")
    cnic = models.IntegerField()
    address = models.TextField(max_length=500,default="")
    phone = models.IntegerField()

    """ this fuction returning back user to admin model """
    def __str__(self):
        return r"User : {0}".format(self.user)