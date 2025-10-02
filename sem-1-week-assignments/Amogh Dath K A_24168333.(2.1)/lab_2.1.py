# LAB_(2.1) ASSIGNMENT WORK.
# STUDENT NAME :- AMOGH DATH K A
# STUDENT ID :- 24168333
# SUBMISSION DATE :- OCT 6TH 2024 



########## TOPIC ###############
# WRITE A PYTHON CODE THAT CALCULATES AN EMPLOYEE'S PAY BASED ON 
# THEIR REGULAR HOURS AND OVERTIME HOURS WORKED IN A WEEK .

# CALCULATION OF PAYMENT

def calculate_employee_payment(name, hours_worked):
    hourly_wage = 22.00  # Given hourly wage as per question is $22.
    regular_hours = 40  # Maximum work per week is 40 hours.
    overtime_rate = 1.5  # Overtime rate is 1.5 times the regular rate as per the question.

    # Calculate regular pay and overtime pay.
    if hours_worked <= regular_hours:
        regular_payment = hours_worked * hourly_wage
        overtime_payment = 0
        overtime_hours = 0
    else:
        regular_payment = regular_hours * hourly_wage
        overtime_hours = hours_worked - regular_hours
        overtime_payment = overtime_hours * hourly_wage * overtime_rate

    # Calculation of total payment.
    total_payment = regular_payment + overtime_payment

    # Result
    print("Employee Name:", name)
    print("Regular Payment:", regular_payment)
    print("Overtime Hours:", overtime_hours)
    print("Overtime Payment:", overtime_payment)
    print("Total Payment:", total_payment)

# Programming logic
print("!!!!Welcome to the Employee Pay Calculator!!!!")
employee_name = str(input("Enter the employee's name: ") )
hours_worked = float(input("Enter the number of hours worked in a week: "))

# Payment calculation function
calculate_employee_payment(employee_name, hours_worked)

# At last, greetings
print("Thank you for using the Employee Pay Calculator .")
print("We hope you will use this calculator again .")

## thank you ##
