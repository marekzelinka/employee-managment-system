"""
Employee management system.
"""

from dataclasses import dataclass
from enum import Enum, auto

FIXED_VACATION_DAYS_PAYOUT = (
    5  # The fixed number of vacation days that can be paid out.
)


class VacationDaysShortageError(Exception):
    """Custom error that is raised when not enough vacations days are available."""

    def __init__(self, requested_days: int, remaining_days: int, message: str) -> None:
        self.requested_days = requested_days
        self.remaining_days = remaining_days
        self.message = message
        super().__init__(message)


class Role(Enum):
    """Emyloyee roles."""

    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()


@dataclass
class Employee:
    """Models a generic company employee."""

    name: str
    role: Role
    vacation_days: int = 25

    # TODO: allow taking holiday spanning multiple days.
    def take_a_holiday(self) -> None:
        """Let the employee take a single holiday."""
        if self.vacation_days < 1:
            raise VacationDaysShortageError(
                requested_days=1,
                remaining_days=self.vacation_days,
                message="You don't have any holidays left. Sorry...",
            )
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")

    def payout_a_holiday(self) -> None:
        """Let the employee get paid for unused holidays"""
        # Check if there are enough vacation days left for a payout
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise VacationDaysShortageError(
                requested_days=FIXED_VACATION_DAYS_PAYOUT,
                remaining_days=self.vacation_days,
                message="You don't have enought holidays left over for a payout.",
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}.")


@dataclass
class HourlyEmployee(Employee):
    """Models a hourly paid company employee."""

    hourly_rate: float = 50
    amount: int = 10


@dataclass
class SalariedEmployee(Employee):
    """Models a fixed salary company employee."""

    monthly_salary: float = 5000


class Company:
    """Models a company with employees."""

    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employees(self, role: Role) -> list[Employee]:
        """Find all employees with a particular role in the employee list."""
        return [employee for employee in self.employees if employee.role is role]

    def pay_employee(self, employee: Employee) -> None:
        """Pay an employee."""
        if isinstance(employee, SalariedEmployee):
            print(
                f"Paying employee {employee.name} a monthly salary of ${employee.monthly_salary}."
            )
        elif isinstance(employee, HourlyEmployee):
            print(
                f"Paying employee {employee.name} a hourly rate of ${employee.hourly_rate} for {employee.amount} hours.."
            )


def main():
    """Main function."""

    company = Company()

    # Add employees to the company
    company.add_employee(SalariedEmployee(name="Louis", role=Role.MANAGER))
    company.add_employee(HourlyEmployee(name="Brenda", role=Role.PRESIDENT))
    company.add_employee(HourlyEmployee(name="Tim", role=Role.INTERN))

    # Print out employees by role
    print(company.find_employees(role=Role.VICEPRESIDENT))
    print(company.find_employees(role=Role.MANAGER))
    print(company.find_employees(role=Role.INTERN))

    # Pay company employee
    company.pay_employee(company.employees[0])

    # Let employee on a vacation
    company.employees[0].take_a_holiday()


if __name__ == "__main__":
    main()
