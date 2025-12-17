from employee import Employee, Role


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
