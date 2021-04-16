from django.test import SimpleTestCase,TestCase
from InventoryApp.models import *

class TestEquipmentModel(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Equipment.objects.create(name='Samsung12')

    def test_str_method(self):
        new_entry=Equipment(name="lenevo")
        self.assertEqual(str(new_entry),new_entry.name)

    def test_name(self):
        equipment = Equipment.objects.get(id=1)
        field_label = equipment._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')
