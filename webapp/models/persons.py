from django.db import models
import json


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    worker_id = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    position = models.IntegerField(default=1, null=True, blank=True)
    password = models.CharField(default='123123123', max_length=100, null=True, blank=True)

    class Meta:
        app_label = 'webapp'
        db_table = 'person'

    @classmethod
    def create(cls):
        person = Person.objects.create()
        return person

    @classmethod
    def find_by_person_id(cls, person_id):
        try:
            user = Person.objects.get(person_id=person_id)
            return user
        except Person.DoesNotExist:
            return False

    @classmethod
    def login(cls, worker_id, password):
        try:
            user = Person.objects.get(worker_id=worker_id)
            if user and (user.password == password):
                return user
            return False
        except Person.DoesNotExist:
            return False

    @classmethod
    def find_all_person_info(cls):
        users = Person.objects.all()
        return list(users)

    @classmethod
    def find_by_worker_id(cls, worker_id):
        try:
            user = Person.objects.get(worker_id=worker_id)
            return user
        except Person.DoesNotExist:
            return False
