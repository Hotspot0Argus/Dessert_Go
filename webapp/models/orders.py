from django.db import models


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    table_id = models.CharField(max_length=20, null=True, blank=True)
    customer_num = models.IntegerField(null=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    # '{menu_list:[{menu_id,menu_name,menu_price,menu_num}]}'
    menu_list = models.TextField(null=True, blank=True)
    # finished ing err
    status = models.CharField(max_length=15, null=True, blank=True)
    person_id = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'webapp'
        db_table = 'orders'
