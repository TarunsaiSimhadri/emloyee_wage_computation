"""

@Author: Tarunsai
@Date: 2024-07-16
@Last Modified by:
@Last Modified time:
@Title : Employee wage computation.

"""


import random

WAGE_PER_HOUR = 20  
FULL_DAY_WORKING_HOURS = 8

def check_attendance():


    """
    description:
        This function is used to check attendance.
    parameters:
        None
    return:
        employee_attendance
    """    


    attendance = random.randint(0, 1)

    if attendance == 1:
        employee_attendance = 'present'

    else:
        employee_attendance = 'absent'
    
    return employee_attendance


def calculate_full_time_employee_wage_per_day(check_attendance):


    """
    description:
        This function is used to calculate employee wage for full time employees.
    parameters:
        check_attendance - to check attendance and calculate wage
    return:
        employee_wage_per_day
    """ 

    
    if check_attendance == 'present':
        employee_wage_per_day = WAGE_PER_HOUR*FULL_DAY_WORKING_HOURS

    else:
        employee_wage_per_day = 0

    return employee_wage_per_day


def main():
    emp_attendance = check_attendance()
    emp_wage = calculate_full_time_employee_wage_per_day(emp_attendance)
    

if __name__ == '__main__':
    main()