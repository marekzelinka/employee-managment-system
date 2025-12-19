from employees.employee import Employee, Role


class Company:
    """Models a company with employees."""

    def __init__(self) -> None:
        self.employees: list[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employees(
        self, role: Role | None = None, name: str | None = None
    ) -> list[Employee]:
        """Find all employees with a particular role and/or name in the employee list."""
        return [
            employee
            for employee in self.employees
            if (role is None or employee.role is role)
            and (name is None or name.lower() in employee.name.lower())
        ]
