# LAB_(2.2) ASSIGNMENT WORK.
# STUDENT NAME :- AMOGH DATH K A
# STUDENT ID :- 24168333
# SUBMISSION DATE :- OCT 6TH 2024 

########## TOPIC ###############

# WRITE A PYTHON CODE TO DETERMINE WHETHER A GIVEN YEAR IS A LEAP YEAR . A YEAR IS A LEAP YEAR IF ANY OF THE FOLLOWING SATISFIES.
# 01. THE YEAR IS MULTIPLE OF 400.
# 02. THE YEAR IS A MULTIPLE OF 4 BUT NOT A MULTIPLE OF 100 .

def is_leap_year(year):
    # A year is a leap year if it is divisible by 400,
    # or if it is divisible by 4 but not by 100.
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)  # BOOLEAN OPERATION IS USED .

# TAKE YEAR INPUT FROM THE USER #
year = int(input("Enter a year: "))

# Check if the year is a leap year and print the result
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")


print (" Thank you for using the leap year calculator.")
print (" Visit us again to calculate leap year again .")
### THANK YOU ###