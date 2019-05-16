from django.db import models
import datetime


class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    order_id = models.IntegerField(null=True, blank=True)
    person_id = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'webapp'
        db_table = 'logs'

    @classmethod
    def new_log_create(cls, order_id, person_id):
        new_log = Log.objects.create(order_id=order_id, person_id=person_id)
        new_log.save()
        return True

    @classmethod
    def find_logs(cls, person_id):
        logs = Log.objects.filter(person_id=person_id)
        return logs

    @classmethod
    def change_log(cls, person_id):
        log = Log.objects.filter(person_id=person_id, order_id=None, end_time=None)
        log['end_time'] = datetime.datetime.now()
        return True
