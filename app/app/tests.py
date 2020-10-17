from django.test import TestCase
from app.calc import add, subtract


class CalcTests(TestCase):

    def test_add_numbers(self):
        """test two numbers added together"""
        self.assertEqual(add(7, 34), 41)

    def test_subtract_numbers(self):
        """test two numbers subtracted and return"""
        self.assertEqual(subtract(78, 50), 28)
