class Employee:
    def __init__(self, first_name, last_name, salary, shift):
        self._first_name = first_name
        self._last_name = last_name
        self.salary = salary
        # Composition: Make association between Employee sublclass and Shift subclass
        self.shift = shift

    # Encapsulation: client does not need to know about first and last name
    def get_full_name(self):
        return f"{self._last_name}, {self._first_name}"

    def raise_salary(self, amount):
        self.salary = self.salary + amount


# Inheritance: sub classes inherit from parent class and set their own attributes
class Mechanic(Employee):
    # Polymorphism
    job_title = "Mechanic"


class Manager(Employee):
    job_title = "Manager"


class StationAttendant(Employee):
    job_title = "Station Attendant"


class Cook(Employee):
    job_title = "Cook"