class Report:
    # Dependency injection: the dependencies are input when instantiating the object. I this way, the report is
    # decoupled from
    def __init__(self, emp_list):
        self._emp_list = emp_list


class StaffingReport(Report):

    # Polymorphism: method name is shared in subclasses, but behaviour depends on subclass
    def print_report(self):
        print("Staffing")
        print("==========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.job_title}")


class AccountingReport(Report):

    # Polymorphism: method name is shared in subclasses, but behaviour depends on subclass. No if/else blocks needed
    # to choose specific method name for subclass
    def print_report(self):
        print("Accounting")
        print("==========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, ${e.salary}")


class ScheduleReport(Report):

    def print_report(self):
        print("Schedule")
        print("==========")
        for e in self._emp_list:
            print(f"{e.get_full_name()}, {e.shift.get_shift_info()}")
