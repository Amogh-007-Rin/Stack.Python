## LAB ASSIGNMENT :- 6.1 ( WEEK 6 LAB ACTIVITY 1 )
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333


####################### TOPIC #######################

### Create a test table for the Bank exercise in Week 3.###


def create_test_table():
    test_cases = [
        {"name": "NAME 1", "choices": [(1, 500), (4,)], "expected": ["£500 deposited. New balance: £1500", "Goodbye!"]},
        {"name": "NAME 2", "choices": [(2, 200), (3,), (4,)], "expected": ["£200 withdrawn. New balance: £800", "Balance: £800", "Goodbye!"]},
        {"name": "NAME 3", "choices": [(2, 1200), (4,)], "expected": ["Error: Insufficient funds", "Goodbye!"]},
        {"name": "NAME 4", "choices": [(3,), (4,)], "expected": ["Balance: £1000", "Goodbye!"]},
        {"name": "NAME 5", "choices": [(5,), (4,)], "expected": ["Invalid option. Please choose (1-4)", "Goodbye!"]} ]
    
    
    for i, test in enumerate(test_cases):
        print(f"\nTest Case {i + 1}: {test['name']}")
        for choice in test["choices"]:
            if len(choice) == 2:
                print(f"Choice: {choice[0]}, Amount: {choice[1]}")
            else:
                print(f"Choice: {choice[0]}")
        print("Expected Output:")
        for expected in test["expected"]:
            print(expected)


def main():
    balance = 1000
    
    print("WELCOME TO OUR BANK")
    
    name = input("ENTER YOUR NAME : ")
    print(f"Welcome, {name}")
    
    while True:
        print("\nPLEASE CHOOSE AN OPTION :")
        print("1.DEPOSITE MONEY")
        print("2.WITHDRAW MONEY")
        print("3.CHECK BALLENCE")
        print("4.QUIT")
        
        option = int(input("(ENTER YOUR CHOICE "))
        
        if option == 1:
            amount = float(input("ENTER AMOUNT TO DEPOSITE: "))
            balance += amount
            print(f"£{amount} DEPOSITED. NEW BALLENCE : £{balance}")
        
        elif option == 2:
            amount = float(input("ENTER AMOUNT TO WITHDRAW : "))
            if amount > balance:
                print("ERROR: INSUFFICIENT FUNDS") 
            else:
                balance -= amount
                print(f"£{amount} WITHDRAWN . NEW BALANCE : £{balance}")
        
        elif option == 3:
            print(f"BALANCE: £{balance}")
        
        elif option == 4:
            print("GOODBYE!")
            break
        
        else:
            print("INVALID OPTION , PLEASE CHOOSE ONE OF THE OPTION FROM (1-4).")

if __name__ == "__main__":
    create_test_table()
    main()
