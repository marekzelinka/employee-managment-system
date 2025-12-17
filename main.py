"""
Employee management system.
"""

from abc import ABC, abstractmethod
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
class Employee(ABC):
    """Models a generic company employee."""

    name: str
    role: Role
    vacation_days: int = 25

    @abstractmethod
    def pay(self) -> None:
        """Method to call when paying an employee."""
        ...

    def take_time_off(self, days: int = 1) -> None:
        """Let the employee take a `n` days of paid time off, where n defaults 1."""
        if self.vacation_days < days:
            raise VacationDaysShortageError(
                requested_days=days,
                remaining_days=self.vacation_days,
                message="You don't have any paid time off days left. Sorry...",
            )
        self.vacation_days -= days
        print(f"Have fun on your vacation, {self.name}.")

    def payout_a_holiday(self) -> None:
        """Let the employee get paid for unused holidays."""
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
    hours_worked: int = 10

    def pay(self) -> None:
        # TODO: format currency
        print(
            f"Paying employee {self.name} a hourly rate of \
            ${self.hourly_rate} for {self.hours_worked} hours.."
        )


@dataclass
class SalariedEmployee(Employee):
    """Models a fixed salary company employee."""

    monthly_salary: float = 5000

    def pay(self) -> None:
        print(
            f"Paying employee {self.name} a monthly salary of ${self.monthly_salary}."
        )


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
    company.employees[0].pay()

    # Let employee on a vacation
    company.employees[0].take_time_off()
    company.employees[0].take_time_off(days=4)


if __name__ == "__main__":
    main()
