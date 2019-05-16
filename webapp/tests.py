from django.test import TestCase
from webapp.models import Menu


# Create your tests here.
class MenuTestCase(TestCase):
    def setUp(self):
        Menu.objects.create(name='123', price=15)
        Menu.objects.create(name='321', price=51)

    def test_menu_info(self):
        item1 = Menu.objects.get(name='123')
        item2 = Menu.objects.get(name='321')
        self.assertEqual(item1.get_obj(), {'name': '123', 'price': 15})
        self.assertEqual(item2.get_obj(), {'name': '321', 'price': 51})
