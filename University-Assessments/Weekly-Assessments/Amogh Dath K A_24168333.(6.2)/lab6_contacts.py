## LAB ASSIGNMENT :- 6.2( WEEK 6 LAB ACTIVITY 2 )
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333


####################### TOPIC #######################

### MAKING A CONTACTS SAVING SYSTEM USING PYTHON PROGRAMMING ###

class ContactApp:
    def __init__(self):
        self.contacts = {
            1: {'NAME': 'STISH', 'NUMBER': 123},
            2: {'NAME': 'RITA', 'NUMBER': 321}
        }
        self.next_id = 3

    def view_contacts(self):
        print("------ VIEW_CONTACTS ------")
        for contact_id, contact in self.contacts.items():
            print(f"{contact['NAME']} {contact['NUMBER']} {contact_id}")
        print("---------------------------")

    def add_contact(self):
        name = input("ENTER CONTACT NAME : ")
        number = input("ENTER CONTACT NUMBER : ")
        self.contacts[self.next_id] = {'NAME': name, 'NUMBER': int(number)}
        print(f"{name} HAS BEEN ADDED INTO THE CONTACT .")
        self.next_id += 1

    def delete_contact(self):
        contact_id = int(input("ENTER THE ID OF THE CONTACT TO DELETE : "))
        if contact_id in self.contacts:
            del self.contacts[contact_id]
            print(f"DELETED: RECORD {contact_id}")
        else:
            print("INVALID ID")

    def main(self):
        while True:
            print("\nSELECT AN OPTION DISPLAYED BELLOW :")
            print("v VIEW CONTACTS ")
            print("a ADD CONTACTS")
            print("d DELETE CONTACTS")
            print("q QUIT ")
            choice = input("ENTER CHOICES (v/a/d/q): ").strip().lower()
            if choice == 'v':
                self.view_contacts()
            elif choice == 'a':
                self.add_contact()
            elif choice == 'd':
                self.delete_contact()
            elif choice == 'q':
                print("------ GOODBYE SEE YOU AGAIN  ------")
                break
            else:
                print(" INVALID CHOICES ")

if __name__ == "__main__":
    app = ContactApp()
    app.main()
