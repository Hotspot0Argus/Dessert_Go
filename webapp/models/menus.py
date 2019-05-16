from django.db import models


class Menu(models.Model):
    item_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40,null=True, blank=True)
    price = models.IntegerField(default=0,null=True, blank=True)
    # 折扣默认是10 9折就是9 计算的时候 price+offset*0.1 = 单价
    offset = models.IntegerField(default=10,null=True, blank=True)
    # sell-1 not-0
    status = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = 'webapp'
        db_table = 'menus'

    @classmethod
    def create_new_item(cls):
        new_item = Menu.objects.create()
        return new_item

    @classmethod
    def find_all_items(cls):
        items = Menu.objects.all()
        return items

    @classmethod
    def find_item(cls, item_id):
        item = Menu.objects.get(item_id=item_id)
        return item

    @classmethod
    def remove_item(cls, item_id):
        Menu.objects.filter(item_id=item_id).delete()
        return 1
