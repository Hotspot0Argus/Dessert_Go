from django.db import models


class Person(models.Model):
    person_id = models.AutoField(primary_key=True)
    worker_id = models.CharField(max_length=20, null=True, blank=True)
    name = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=40, null=True, blank=True)
    position = models.IntegerField(default=1, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        app_label = 'webapp'
        db_table = 'person'

    @classmethod
    def create(cls):
        person = Person.objects.create()
        return person.person_id

    @classmethod
    def find_by_person_id(cls, person_id):
        user = Person.objects.get(person_id=person_id)
        return user

    @classmethod
    def find_all_person_info(cls):
        users = Person.objects.all()
        return users
