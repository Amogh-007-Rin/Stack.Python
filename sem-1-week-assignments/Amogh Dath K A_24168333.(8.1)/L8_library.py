## LAB ASSIGNMENT :- 8.1( WEEK 8 LAB ACTIVITY 1 )
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333


####################### TOPIC #######################

### . Create a list of 2 bank accounts, and implement the following batch operations:###
#• Set all account initial money with 100.
#• Withdraw 40 respectively.
#• Display balance for all accounts.
#• Deposit 20 respectively.
#• Display balance for all accounts.
#• Transfer 20 from second account to the first one
#• Display balance for all accounts.

class BankAccount:
    def __init__(self, acc_number, balance=0.0):
        self.acc_number = acc_number
        self.balance = balance

    def get_account(self):
        return self.acc_number

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("Please enter a positive amount to deposit.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient balance or invalid amount.")

    def transfer(self, amount, other_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            other_account.deposit(amount)
        else:
            print("Insufficient balance or invalid amount.")

from L8_library import BankAccount

def main():
    # Create two bank accounts
    account1 = BankAccount(1, 100)
    account2 = BankAccount(2, 100)

    # Withdraw 40 from each account
    account1.withdraw(40)
    account2.withdraw(40)

    # Display balances
    print(f"Account 1 balance: {account1.get_balance()}")
    print(f"Account 2 balance: {account2.get_balance()}")

    # Deposit 20 to each account
    account1.deposit(20)
    account2.deposit(20)

    # Display balances again
    print(f"Account 1 balance: {account1.get_balance()}")
    print(f"Account 2 balance: {account2.get_balance()}")

    # Transfer 20 from account 2 to account 1
    account2.transfer(20, account1)

    # Display final balances
    print(f"Account 1 balance: {account1.get_balance()}")
    print(f"Account 2 balance: {account2.get_balance()}")

if __name__ == "__main__":
    main()
