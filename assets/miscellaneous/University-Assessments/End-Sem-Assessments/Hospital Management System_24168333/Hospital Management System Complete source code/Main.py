# Imports
from Admin import Admin
from Doctor import Doctor
from Patient import Patient

def main():
    """
    the main function to be ran when the program runs
    """

    # Initialising the commands
    admin = Admin.load_admin_details_from_file() # username is 'admin', password is '123' if in case the password is not working try to enter the password as '456'
    doctors = [Doctor('John','Smith','Internal Med.'), Doctor('Jone','Smith','Pediatrics'), Doctor('Jone','Carlos','Cardiology')]
    patients = admin.load_patient_data_from_file()
    if not patients:
        patients = [
            Patient('Sara', 'Smith', 20, '07012345678', 'B1 234', ['cold', 'cough']),
            Patient('Mike', 'Jones', 37, '07555551234', 'L2 2AB', ['Sore Throat']),
            Patient('David', 'Smith', 15, '07123456789', 'C1 ABC', ['headache', 'Fever'])
        ]

    discharged_patients = []

    # keep trying to login till the login details are correct
    while True:
        if admin.login():
            running = True # allow the program to run
            break
        else:
            print('Incorrect username or password.')

    while running:
        # print the menu
        print('Please Select an option:')
        print(' 1- Register/view/update/delete doctor')
        print(' 2- Patient Management')
        print(' 3- Discharge patients')
        print(' 4- View discharged patient')
        print(' 5- Assign doctor to a patient')
        print(' 6- View assigned patients')
        print(' 7- Update admin details')
        print(' 8- Groups of patients By Surname')
        print(' 9- Save patient data to file')
        print(' 10- Generate Management Report')
        print(' 11- Quit')

        # get the option
        op = input('Option: ')

        if op == '1':
            # 1- Register/view/update/delete doctor
         #ToDo1
            admin.doctor_management(doctors)
        elif op == '2':
            admin.patient_management(patients)
        
        elif op == '3':
            # 2- View or discharge patients
            #ToDo2
            admin.discharge(patients, discharged_patients)

            while True:
                op = input('Do you want to discharge a patient(Y/N):').lower()

                if op == 'yes' or op == 'y':
                    #ToDo3
                    admin.discharge(patients, discharged_patients)

                elif op == 'no' or op == 'n':
                    break

                # unexpected entry
                else:
                    print('Please answer by yes or no.')
        
        elif op == '4':
            # 3 - view discharged patients
            #ToDo4
            admin.view_discharge(discharged_patients)
        elif op == '5':
            # 4- Assign doctor to a patient
            admin.assign_doctor_to_patient(patients, doctors)
        elif op == '6':
            admin.view_doctor_patients(doctors)
        elif op == '7':
            # 5- Update admin detais
            admin.update_details()
        elif op == '8':
            admin.group_patients_by_surname(patients)
        elif op == '9':

            admin.save_patient_data_to_file(patients)
        elif op == '10':
            admin.generate_management_report(doctors, patients)
        elif op == '11':
            # 6 - Quit
            #ToDo5
            print('Exiting the program.')
            running = False

        else:
            # the user did not enter an option that exists in the menu
            print('Invalid option. Try again')

if __name__ == '__main__':
    main()
