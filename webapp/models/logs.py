from django.db import models
import datetime


class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    order_id = models.IntegerField(null=True, blank=True)
    person_id = models.IntegerField(null=True, blank=True)
    person_name = models.CharField(max_length=50, null=True, blank=True)

    class Meta:
        app_label = 'webapp'
        db_table = 'logs'

    @classmethod
    def create(cls, order_id, person_id, person_name):
        new_log = Log.objects.create(order_id=order_id, person_id=person_id, person_name=person_name)
        new_log.save()
        return True

    @classmethod
    def find_logs(cls):
        logs = Log.objects.order_by('start_time')
        return list(logs)

    @classmethod
    def change_log(cls, person_id):
        log = Log.objects.filter(person_id=person_id, order_id=None, end_time=None)
        log = list(log)
        log[0].end_time = datetime.datetime.now()
        log[0].save()
        return True

    @classmethod
    def create_order(cls, order_id, person_id, person_name):
        new_log = Log.objects.create(order_id=order_id, person_id=person_id, person_name=person_name,
                                     end_time=datetime.datetime.now())
        new_log.save()
        return True
