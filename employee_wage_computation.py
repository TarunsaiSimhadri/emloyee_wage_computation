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
PART_TIME_WAGE = 15
PART_TIME_WORKING_HOURS = 8

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


def employee_type_wage_per_day(employee_type):


    """
    description:
        This function is used to find employee type and wage accordingly.
    parameters:
        employee_type - according to that type generate employee wage
    return:
        employee_wage_per_day, else : enter correct employee_type
    """    



    if employee_type == 'FULL-TIME':
        employee_wage_per_day = WAGE_PER_HOUR * FULL_DAY_WORKING_HOURS
        return employee_wage_per_day
    
    elif employee_type == 'PART-TIME':
        employee_wage_per_day = PART_TIME_WAGE * PART_TIME_WORKING_HOURS
        return employee_wage_per_day
    
    else:
        return "enter correct employee_type"
        
   
def main():
    emp_attendance = check_attendance()
    print(emp_attendance)
    wage_per_day = 0

    if emp_attendance == 'present':
        employee_type = input("enter FULL-TIME/PART-TIME: ").upper()
        wage_per_day = employee_type_wage_per_day(employee_type)
        print(f"employee wage is {wage_per_day}")
    else:
        print(f"employee wage is {wage_per_day}")    




if __name__ == '__main__':
    main()