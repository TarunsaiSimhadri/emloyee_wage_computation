"""

@Author: Tarunsai
@Date: 2024-07-16
@Last Modified by:
@Last Modified time:
@Title : Employee wage computation.

"""


import random

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


def main():
    check_attendance = check_attendance()
    print(check_attendance)


if __name__ == '__main__':
    main()