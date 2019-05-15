from django.db import models


class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    order_id = models.IntegerField(default=0, null=True, blank=True)
    worker_id = models.CharField(max_length=30)

    class Meta:
        app_label = 'webapp'
        db_table = 'Log'

    #     函数未写
