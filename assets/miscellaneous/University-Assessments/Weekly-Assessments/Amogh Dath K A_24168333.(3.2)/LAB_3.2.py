## LAB ASSIGNMENT :- 3.2
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333

####################### TOPIC #######################

# CREAT A PYTHON PROGRAM THAT PROMPTS THE USER FOR A PASSWORD . 
# IT WILL KEEP ASKING FOR THE PASSWORD UNTIL EITHER THE CORRECT PASSWORD "test100" IS PROVIDED.
# OR THE USER ATTEMPTS TO ENTER THE PASSWORD UPTO 5 TIME .

## PROGRAM ## 
## PASSWORD = (test100)

def password_prompt():
    correct_password="test100"
    maximum_attempts = 5
    attempts = 0


    while attempts < maximum_attempts:
        password=input("ENTER YOUR PASSWORD:-->")
        if password == correct_password:
            print("PASSWORD CORRECT")
            print("...YOUR ARE LOGGED INTO YOUR ACCOUNT...")
            break
        else:
            attempts= 1 + attempts
            print(f"INCORRECT PASSWORD. YOU HAVE{maximum_attempts - attempts} ATTEMPTS LEFT..")

        if attempts == maximum_attempts:
                print(" YOU've REACHED MAXIMUM LOGIN ATTEMPTS.")
                print(" LOGIN FAILED FOR YOUR ACCOUNT. ")
                print("PLEASE TRY AGAIN AFTER SOMETIME.")
if __name__ == "__main__":
            
            password_prompt()
