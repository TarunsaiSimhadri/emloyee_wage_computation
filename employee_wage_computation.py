"""

@Author: Tarunsai
@Date: 2024-07-16
@Last Modified by:
@Last Modified time:
@Title : Employee wage computation.

"""


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
    


def main():
    emp1 = Employee("tarun", 20)
    emp2 = Employee("varun", 30)
    emp3 = Employee("kamal", 20)

    emp1.monthly_wage()
    emp2.monthly_wage()
    emp3.monthly_wage()

    com1 = Company("tcs")
    com2 = Company("wipro")
    com3 = Company("apexon")

    com1.add_employee(emp1)
    com2.add_employee(emp2)
    com3.add_employee(emp3)


if __name__ == '__main__':
    main()