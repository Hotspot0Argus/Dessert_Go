from django.db import models


class Log(models.Model):
    log_id = models.AutoField(primary_key=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(auto_now=True)
    order_id = models.IntegerField(default=0, null=True, blank=True)
    person_id = models.IntegerField()

    class Meta:
        app_label = 'webapp'
        db_table = 'logs'

    @classmethod
    def new_log_create(cls):
        new_log = Log.objects.create()
        new_log.save()
        return new_log

    @classmethod
    def find_logs(cls,person_id):
        logs = Log.objects.filter(person_id=person_id)
        return logs
