"""
Employee management system.
"""

from dataclasses import dataclass

FIXED_VACATION_DAYS_PAYOUT = (
    5  # The fixed number of vacation days that can be paid out.
)


@dataclass
class Employee:
    """Models a generic company employee."""

    name: str
    role: str
    vacation_days: int = 25

    def take_a_holiday(self, payout: bool) -> None:
        """Let the employee take a single holiday, or pay ou 5 holidays."""
        if payout:
            # Check if there are enough vacation days left for a payout
            if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError(
                    f"You don't have enought holidays left over for a payout. Remaining holidays: {self.vacation_days}."
                )
            try:
                self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
                print(f"Paying out a holiday. Holidays left: {self.vacation_days}.")
            except Exception:
                pass
        else:
            if self.vacation_days < 1:
                raise ValueError(
                    "You don't have any holidays left. Now back to work, you!"
                )
            self.vacation_days -= 1
            print("Have fun on your holiday. Don't forget to check your emails!")


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

    def find_managers(self) -> list[Employee]:
        """Find all manager employees."""
        managers: list[Employee] = []
        for employee in self.employees:
            if employee.role == "manager":
                managers.append(employee)
        return managers

    def find_vice_presidents(self) -> list[Employee]:
        """Find all vice-president employees."""
        vice_presidents: list[Employee] = []
        for employee in self.employees:
            if employee.role == "vice_president":
                vice_presidents.append(employee)
        return vice_presidents

    def find_interns(self) -> list[Employee]:
        """Find all interns."""
        interns: list[Employee] = []
        for employee in self.employees:
            if employee.role == "intern":
                interns.append(employee)
        return interns

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

    # Define our employees
    louis = SalariedEmployee(name="Louis", role="manager")
    brenda = HourlyEmployee(name="Brenda", role="president")
    tim = HourlyEmployee(name="Tim", role="intern")

    # Add our employees to the company
    company.add_employee(louis)
    company.add_employee(brenda)
    company.add_employee(tim)

    # Print out employees by role
    print(company.find_managers())
    print(company.find_vice_presidents())
    print(company.find_interns())

    # Pay company employee
    company.pay_employee(company.employees[0])

    # Let employee on a vacation
    company.employees[0].take_a_holiday(False)


if __name__ == "__main__":
    main()
