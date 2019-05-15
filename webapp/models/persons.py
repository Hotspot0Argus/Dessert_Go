from django.db import models


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    worker_id = models.CharField(max_length=20)
    name = models.CharField(max_length=40)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=40)
    position = models.IntegerField(default=1)
    password = models.CharField(max_length=100)

    class Meta:
        app_label = 'webapp'
        db_table = 'person'

    @classmethod
    def check_worker_id_and_person_id(cls, person_id, worker_id):
        return True

    @classmethod
    def find_by_person_id(cls, person_id):
        user = Person.objects.get(person_id=person_id)
        return user

    @classmethod
    def find_all_person_info(self):
        users = Person.objects.all()
        return users
