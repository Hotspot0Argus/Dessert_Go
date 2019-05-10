# from __future__ import unicode_literals

from django.db import models
#
# # Create your models here.
class MenuInfo(models.Model):
    name=models.CharField(max_length=200)
    price=models.IntegerField(default=0)


    def get_obj(self):
        return{'name':self.name,'price':self.price}