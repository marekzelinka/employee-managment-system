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
        filtered = self.employees
        if role:
            filtered = [employee for employee in filtered if employee.role is role]
        if name:
            filtered = [
                employee
                for employee in filtered
                if name.lower() in employee.name.lower()
            ]
        return filtered
