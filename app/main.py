"""
Employee management system.
"""

from company import Company
from employee import HourlyEmployee, Role, SalariedEmployee


def main():
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
