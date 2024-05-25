"""
Sample tests
"""

from django.test import SimpleTestCase

from app import calc


class CalcTests(SimpleTestCase):
    """Test the calc module"""

    def test_add_numbers(self):
        """Test adding numbers"""
        res = calc.add(5, 6)

        self.assertEquals(res, 11)

    def test_sub_numbers(self):
        res = calc.sub(10, 15)

        self.assertTrue(res, 5)
