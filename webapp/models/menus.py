from django.db import models


class Menu(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.IntegerField(default=0)
    # 折扣默认是10 9折就是9 计算的时候 price+offset+10 = 单价
    offset = models.IntegerField(default=10)
    status = models.CharField(max_length=15)

    class Meta:
        app_label = 'webapp'
        db_table = 'Menu'
