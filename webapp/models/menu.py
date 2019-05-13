from django.db import models


class Menu(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)

    class Meta:
        app_label = 'webapp'
        db_table = 'menu'

    def get_obj(self):
        return {'name': self.name, 'price': self.price}
