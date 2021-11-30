import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    def test_get_full_name(self):
        e = Employee("John", "Doe", 0, None)
        self.assertEqual(e.get_full_name(), "Doe, John")

    def test_raise_salary(self):
        e = Employee("John", "Doe", 0, None)
        e.raise_salary(500)
        self.assertEqual(e.salary, 500)