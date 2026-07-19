## LAB ASSIGNMENT :- 4.1
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333

#################################################################################### TOPIC ####################################################################################
                     ## CREATE A CALCULATOR PROGRAM ##
# Create a program that takes three parameters; two numbers and one string. The string is used to indicate the arithmetic operation to apply on the two numbers.

# Function to take user input and return two integers and an operator as a tuple
def get_input():
    num1 = int(input("Enter the first integer: "))
    num2 = int(input("Enter the second integer: "))
    operator = input("Enter an operator ( for addition (+),for multiplication (*) for difference (-) for division (/)): ")
    return num1, num2, operator

## Let the two numbers be (x & y) as a input variable ##

# Function to add two integers and print the result
def add_numbers(x, y):
    result = x + y
    print(f"The sum of {x} and {y} is {result}")

# Function to multiply two integers and print the result
def multiply_numbers(x, y):
    result = x * y
    print(f"The product of {x} and {y} is {result}")

# Function to subtract two integers and print the result
def subtract_numbers(x,y):
    result = x-y
    print(f"the diffrence of {x} and {y} is {result}")

# Function to division two intergers and print the result
def divide_numbers(x,y):
    result = x/y
    print(f"the division value of {x} and {y} is {result} ")

# Main function to coordinate the operations
def main():
    print("Basic Calculator")
    num1, num2, operator = get_input()
    
    if operator == '+':
        add_numbers(num1, num2)
    elif operator == '*':
        multiply_numbers(num1, num2)
    elif operator == '-':
        subtract_numbers(num1, num2)
    elif operator == '/':
        divide_numbers(num1,num2)


    else:
        print("Invalid operator. Please use (+) or (*) or (-) or (/) to continue the calculations .")

# Run the main function
if __name__ == "__main__":
    main()




### the following are the modifications of the code for the excercise 4.1 and the result will be displayed in the terminal ###


