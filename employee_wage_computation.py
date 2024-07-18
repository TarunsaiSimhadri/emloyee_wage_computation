import random

class Employee:

    FULL_DAY_HOURS = 8
    PART_TIME_HOURS = 4
    WORKING_DAYS_PER_MONTH = 20
    MAX_WORKING_HOURS = 100

    def __init__(self, name, wage_per_hr):
        self.emp_name = name
        self.wage_per_hr = wage_per_hr
        self.total_hrs_worked = 0
        self.total_days_worked = 0
        self.total_wage = 0    
    
    @staticmethod    
    def get_attendance():
        return random.randint(0, 2)
    
    
    def daily_wage(self):
        emp_status = self.get_attendance()
    
        if emp_status == 0:
            return 0,0
        elif emp_status == 1: 
            return self.wage_per_hr * self.FULL_DAY_HOURS, self.FULL_DAY_HOURS
        elif emp_status == 2:
            return self.wage_per_hr * self.PART_TIME_HOURS, self.PART_TIME_HOURS
            
    def monthly_wage(self):
        while self.total_days_worked < self.WORKING_DAYS_PER_MONTH and self.total_hrs_worked < self.MAX_WORKING_HOURS:
            wage, hours = self.daily_wage()
            # print(wage)
            self.total_wage += wage
            self.total_hrs_worked += hours
            self.total_days_worked += 1

    def get_emp_details(self):
        print(f"Name: {self.emp_name}")
        print(f"Total Wage: {self.total_wage}") 
        print(f"Total Hours Worked: {self.total_hrs_worked}")
        print(f"Total Days Worked: {self.total_days_worked}")


class Company:
    def __init__(self, name) -> None:
        self.company_name = name
        self.employee_dict = {}

    def get_employee(self, emp_name):
        return self.employee_dict.get(emp_name)

    def add_employee(self, emp_obj):
        self.employee_dict.update({emp_obj.emp_name: emp_obj})

    def delete_employee(self, emp_name):
        self.employee_dict.pop(emp_name)
    
    def display_emp_details(self):
        for emp in self.employee_dict.values():
            emp.get_emp_details()
            print("="*50)

class MultipleCompanies:
    def __init__(self) -> None:
        self.company_dict = {}

    def get_company(self, comp_name):
        if comp_name not in self.company_dict:
            return None
        return self.company_dict[comp_name]

    def add_company(self, com_obj):
        self.company_dict.update({com_obj.company_name: com_obj})

    def delete_company(self, company_name):
        self.company_dict.pop(company_name)

    def display_company(self):
        for com in self.company_dict.values():
            print("*"*50)
            print(f"Company: {com.company_name}")
            com.display_emp_details()

def main():
    multi_comp = MultipleCompanies()

    while True:
        choice = int(input("Enter 0 to exit: "))
        if choice == 0:
            break

        if choice == 1:
            company_name = input("Enter company name: ")
            company = multi_comp.get_company(company_name)
            if not company:
                company = Company(company_name)

            emp_name = input("Enter employee name: ")
            employee = company.get_employee(emp_name)
            if not employee:
                wage_per_hr = int(input("ENter wage: "))
                employee = Employee(emp_name, wage_per_hr)
                employee.monthly_wage()

            company.add_employee(employee)
            multi_comp.add_company(company)
        if choice == 2:
            multi_comp.display_company()
        if choice ==3:
            company_name = input('enter company_name: ')
            multi_comp.delete_company(company_name)
        if choice == 4:
            company_name = input("Enter company name: ")
            company = multi_comp.get_company(company_name)
            if not company:
                print("company not found")
                continue
            emp_name = input('enter employee name: ')
            company.delete_employee(emp_name)
            

if __name__ == '__main__':
    main()