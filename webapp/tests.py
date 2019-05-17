from django.test import TestCase
from webapp.models import logs


# Create your tests here.
class MenuTestCase(TestCase):
    def setUp(self):
        logs.Log.objects.create(
            order_id=1,
            person_id=1,
            person_name='123')

    def test_menu_info(self):
        self.assertEqual(logs.Log.find_log(1).order_id, 1)
        self.assertEqual(logs.Log.find_log(1).person_id, 1)
        self.assertEqual(logs.Log.find_log(1).person_name, '123')
