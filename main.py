from employee import Manager, StationAttendant, Cook, Mechanic
from reporting import AccountingReport, StaffingReport, ScheduleReport
from shift import MorningShift, AfternoonShift, NightShift

employees = [
    # Composition: Make association between Employee sublclass and Shift subclass
    Manager("Vera", "Schmidt", 2000, MorningShift()),
    StationAttendant("Chuck", "Norris", 1800, MorningShift()),
    StationAttendant("Samantha", "Carrington", 1800, AfternoonShift()),
    Cook("Roberto", "Jacketti", 2100, MorningShift()),
    Mechanic("Dave", "Dreissig", 2200, MorningShift()),
    Mechanic("Tina", "River", 2300, MorningShift()),
    Mechanic("Ringo", "Rama", 1900, AfternoonShift()),
    Mechanic("Chuck", "Rainey", 1900, NightShift())
]

reports = [
    AccountingReport(employees),
    StaffingReport(employees),
    ScheduleReport(employees)
]


for r in reports:
    r.print_report()
    print()
