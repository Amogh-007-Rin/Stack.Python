## LAB ASSIGNMENT :- 5.2
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333

####################### TOPIC #######################

# Create a Python program to manage the guest list for a party. The program should allow you to add guests,
# remove guests, and print the current guest list

def add_guest(guest_list):
    guest_name = input("ENTER THE NAME OF THE GUEST TO ADD: ")
    guest_list.append(guest_name)
    print(f"{guest_name} HAS BEEN ADDED TO THE LIST .")

def remove_guest(guest_list):
    guest_name = input("ENTER THE NAME OF THE GUEST TO REMOVE: ")
    if guest_name in guest_list:
        guest_list.remove(guest_name)
        print(f"{guest_name} HAS BEEN REMOVED FROM THE GUEST LIST.")
    else:
        print(f"{guest_name} IS NOT ON THE GUEST LIST.")

def print_guest_list(guest_list):
    print("Guest list (sorted alphabetically ascending):")
    for guest in sorted(guest_list):
        print(guest)

def main():
    guest_list = []

    while True:
        print("\nOptions:")
        print("A. ADD A GUEST ")
        print("R. REMOVE A GUEST ")
        print("P. PRINT A GUEST LIST")
        print("Q. QUIT")

        choice = input("ENTER YOUR CHOICE:").upper()

        if choice == 'A':
            add_guest(guest_list)
        elif choice == 'R':
            remove_guest(guest_list)
        elif choice == 'P':
            print_guest_list(guest_list)
        elif choice == 'Q':
            print(f"TOTAL NUMBER OF GUESTS: {len(guest_list)}")
            print("GOODBYE ! SEE YOU SOON AT THE PARTY!")
            break
        else:
            print("INVALID CHOICE . PLEASE CHOOSE A VALID OPTION (A, R, P, or Q).")

# Run the program
if __name__ == "__main__":
    main()
