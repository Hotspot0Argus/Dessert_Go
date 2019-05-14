from django.db import models


class Menu(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    price = models.IntegerField(default=0)
    # 折扣默认是10 9折就是9 计算的时候 price+offset*0.1 = 单价
    offset = models.IntegerField(default=10)
    # sell-1 not-0
    status = models.IntegerField()

    class Meta:
        app_label = 'webapp'
        db_table = 'menu'
