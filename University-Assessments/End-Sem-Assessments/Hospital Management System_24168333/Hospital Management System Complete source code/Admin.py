from Doctor import Doctor
from Patient import Patient
import json
from fpdf import FPDF
from collections import  Counter
from datetime import datetime
import os
import matplotlib.pyplot as plt

class Admin:
    """A class that deals with the Admin operations"""
    def __init__(self, username, password, address = ''):
        """
        Args:
            username (string): Username
            password (string): Password
            address (string, optional): Address Defaults to ''
        """

        self.__username = username
        self.__password = password
        self.__address =  address

    def view(self,a_list):
        """
        print a list
        Args:
            a_list (list): a list of printables
        """
        for index, item in enumerate(a_list):
            print(f'{index+1:3}|{item}')

    def login(self) :
        """
        A method that deals with the login
        Raises:
            Exception: returned when the username and the password ...
                    ... don`t match the data registered
        Returns:
            string: the username
        """
    
        print("-----Login-----")
        #Get the details of the admin

        username = input('Please Enter the username: ')
        password = input('Please Enter the password: ')

        # check if the username and password match the registered ones
        #ToDo1
        if(username == self.__username and password == self.__password):
            print('Login Successful!')
            return username
        else:
            raise Exception("Username or password is incorrect.")

    def find_index(self,index,doctors):
        
            # check that the doctor id exists          
        if index in range(0,len(doctors)):
            
            return True

        # if the id is not in the list of doctors
        else:
            return False
            
    def get_doctor_details(self) :
        """
        Get the details needed to add a doctor
        Returns:
            first name, surname and ...
                            ... the speciality of the doctor in that order.
        """
        #ToDo2
        print("-----Enter Doctor's Details------")
        first_name = input('Please Enter the Doctor\'s first name: ')
        surname = input('Please Enter the doctor\'s surname: ')
        speciality = input('Please Enter the doctor\'s speciality: ')
        return first_name, surname, speciality

    def doctor_management(self, doctors):
        """
        A method that deals with registering, viewing, updating, deleting doctors
        Args:
            doctors (list<Doctor>): the list of all the doctors names
        """

        print("-----Doctor Management-----")

        # menu
        print('Please Choose the operation:')
        print(' 1 - Register Doctor')
        print(' 2 - View Doctor')
        print(' 3 - Update Doctor')
        print(' 4 - Delete Doctor')

        #ToDo3
        op = input('Choose an Option : ')


        # register
        if op == '1':
            print("-----Register-----")

            # get the doctor details
            first_name, surname, speciality = self.get_doctor_details()
            #ToDo4


            # check if the name is already registered
            name_exists = False
            for doctor in doctors:
                if first_name == doctor.get_first_name() and surname == doctor.get_surname():
                    print('Name already exists.')
                    #ToDo5
                    name_exists = True
                    break

            #ToDo6
            if not name_exists:
                new_doctor = Doctor(first_name, surname, speciality)
                doctors.append(new_doctor)
                print('Doctor registered.')

        # View
        elif op == '2':
            print("-----List of Doctors-----")
            #ToDo7
            if len(doctors) > 0:
                print('ID |          Full Name           |  Speciality')
                self.view(doctors)
            else:
                print('No doctors registered.')

        # Update
        elif op == '3':
            while True:
                print("-----Update Doctor`s Details-----")
                print('ID |          Full name           |  Speciality')
                self.view(doctors)
                try:
                    index = int(input('Please Enter the ID of the doctor: ')) -1
                    doctor_index=self.find_index(index,doctors)
                    if doctor_index:
                        doctor = doctors[index]
                        break
                    else:
                        print("Doctor not found")
                    
                        # doctor_index is the ID mines one (-1)
                        

                except ValueError: # the entered id could not be changed into an int
                    print('The ID entered is incorrect')

            # menu
            print('Choose the field to be updated:')
            print(' 1 First name')
            print(' 2 Surname')
            print(' 3 Speciality')
            try:
                op1 = int(input('Input: ')) # make the user input lowercase
                if op1 == 1:
                    new_first_name = input("Please Enter the new first name: ")
                    doctor.set_first_name(new_first_name)
            #ToDo8
                elif op1 == 2:
                    new_surname = input("Please Enter the new surname: ")
                    doctor.set_surname(new_surname)
                elif op1 == 3:
                    new_speciality = input("Please Enter the new speciality: ")
                    doctor.set_speciality(new_speciality)
                else:
                    print("Invalid option chosen. Please select 1,2 or 3.")

                print("Doctor's details updated.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        # Delete
        elif op == '4':
            print("-----Delete Doctor-----")
            print('ID |          Full Name           |  Speciality')
            self.view(doctors)

            try:
                doctor_index = int(input('Please Enter the ID of the doctor to delete: ')) -1
                if doctor_index in range(len(doctors)):
                    doctors.pop(doctor_index)
                    print("Doctor deleted.")
                else:
                    print("The ID entered was not found")
            except ValueError:
                print("Invalid input. Please enter a valid number.")



        # if the id is not in the list of patients
        else:
            print('Invalid operation choosen. Check your spelling!')

    def view_patient(self, patients):
        """
        print a list of patients
        Args:
            patients (list<Patients>): list of all the active patients
        """
        print("-----View Patients-----")
        print('  ID |          Full Name       |     Doctor`s Full Name    | Age |   Mobile     | Postcode |      Symptoms     |')
        for index, patient in enumerate(patients):
            patient_full_name = patient.full_name()
            doctor = patient.get_doctor()
            if isinstance(doctor, Doctor):
                doctor_full_name = f"{doctor.get_first_name()} {doctor.get_surname()}"
            else:
                doctor_full_name = "None"

            age = patient.get_age()
            mobile = patient.get_mobile()
            postcode = patient.get_postcode()
            symptoms = ', '.join(patient.get_symptoms()) if patient.get_symptoms() else "None"
            print(f'{index + 1:3} | {patient_full_name:<25} | {doctor_full_name:<25} | {age:3} | {mobile:<12} | {postcode:<8} | {symptoms:<30}')

    def assign_doctor_to_patient(self, patients, doctors):
        """
        Allow the admin to assign a doctor to a patient
        Args:
            patients (list<Patients>): the list of all the active patients
            doctors (list<Doctor>): the list of all the doctors
        """
        print("-----Assign-----")

        print("-----Patients-----")
        print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms        ')
        self.view(patients)

        patient_index = input('Please enter the patient ID: ')

        try:
            # patient_index is the patient ID mines one (-1)
            patient_index = int(patient_index) -1

            # check if the id is not in the list of patients
            if patient_index not in range(len(patients)):
                print('The id entered was not found.')
                return # stop the procedures

        except ValueError: # the entered id could not be changed into an int
            print('The id entered is incorrect')
            return # stop the procedures

        print("-----Doctors Select-----")
        print('Please Select the doctor that fits these symptoms:')
        patients[patient_index].print_symptoms() # print the patient symptoms

        print('--------------------------------------------------')
        print('ID |          Full Name           |  Speciality   ')
        self.view(doctors)
        doctor_index = input('Please enter the doctor ID: ')

        try:
            # doctor_index is the patient ID mines one (-1)
            doctor_index = int(doctor_index) -1

            # check if the id is in the list of doctors
            if self.find_index(doctor_index,doctors)!=False:

                # link the patients to the doctor and vice versa
                #ToDo11
                selected_patient = patients[patient_index]
                selected_doctor = doctors[doctor_index]
                selected_patient.link(selected_doctor)
                selected_doctor.add_patient(selected_patient)

                print('The patient is now assigned to the doctor.')

            # if the id is not in the list of doctors
            else:
                print('The id entered was not found.')

        except ValueError: # the entered id could not be changed into an in
            print('The id entered is incorrect')


    def discharge(self, patients, discharge_patients):
        """
        Allow the admin to discharge a patient when treatment is done
        Args:
            patients (list<Patients>): the list of all the active patients
            discharge_patients (list<Patients>): the list of all the non-active patients
        """
        print("-----Discharge Patient-----")
        while True:
            print("-----Patients-----")
            print('ID |          Full Name           |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms        ')
            self.view(patients)
            choice = input("Do you want to discharge a patient? (Y/N): ").strip().upper()
            if choice == "N":  # Stop the process if the user inputs "N"
                print("Exiting discharge process.")
                break
        #ToDo12
            elif choice == "Y":
                patient_index = input('Please enter the patient ID to discharge: ').strip()
                try:
                    # Convert the patient ID to a zero-based index
                    patient_index = int(patient_index) - 1

                    # Validate the entered ID
                    if patient_index in range(len(patients)):
                        # Remove the patient from the active list and add to the discharged list
                        discharged_patient = patients.pop(patient_index)
                        discharge_patients.append(discharged_patient)

                        print(f"Patient {discharged_patient.full_name()} has been discharged.")
                    else:
                        print("The ID entered does not exist in the patient list.")

                except ValueError:
                    print("Invalid input. Please enter a valid numeric ID.")
            else:
                print("Invalid choice. Please enter 'Y' or 'N'.")

    def view_discharge(self, discharged_patients):
        """
        Prints the list of all discharged patients
        Args:
            discharged_patients (list<Patients>): the list of all the non-active patients
        """

        print("-----Discharged Patients-----")
        if not discharged_patients:
            print("No patients have been discharged yet.")
            return
        print(' ID |          Full Name        |      Doctor`s Full Name   | Age |    Mobile    | Postcode |      Symptoms        ')
        #ToDo13
        for i,patient in enumerate(discharged_patients,start =1):
            doctor_name = patient.get_doctor() if patient.get_doctor() else "Unassigned"
            symptoms = ', '.join(patient.get_symptoms()) if patient.get_symptoms() else "None"
            print(f'{i:3} | {patient.full_name():<25} | {doctor_name:<25} | {patient.get_age():<3} | {patient.get_mobile():<12} | {patient.get_postcode():<8} | {symptoms:<30}')

    def view_doctor_patients(self, doctors):
        """
        Allows the admin to select a doctor and view their assigned patients
        Args:
            doctors (list<Doctor>): List of all registered doctors
        """
        # Display the list of doctors
        print("----- Doctor List -----")
        print("ID |          Full Name           |  Speciality")
        self.view(doctors)

        try:
            # Prompt user to select a doctor
            doctor_id = int(input("Please Enter the ID of the doctor to view their patients: ")) - 1

            # Validate the selected doctor ID
            if 0 <= doctor_id < len(doctors):
                # Display the selected doctor's assigned patients
                doctors[doctor_id].view_assigned_patients()  # Calls Doctor's method
            else:
                print("Invalid doctor ID. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid numeric ID.")


    def patient_management(self, patients):
        print("-----Patient Management-----")

        # Menu
        print("Please Choose the operation:")
        print(" 1 - Add Patient")
        print(" 2 - View Patient")
        print(" 3 - Update Patient")

        op = input("Choose an Option: ")

        # Add Patient
        if op == '1':
            print("-----Add New Patient-----")
            try:
                first_name = input("Please Enter patient's first name: ").strip()
                surname = input("Please Enter patient's surname: ").strip()
                age = int(input("PLease Enter patient's age: ").strip())
                mobile = input("Please Enter patient's mobile number: ").strip()
                postcode = input("Please Enter patient's postcode: ").strip()
                symptoms = input("Please Enter symptoms (comma-separated): ").split(',')

                new_patient = Patient(first_name, surname, age, mobile, postcode, symptoms)
                patients.append(new_patient)
                print("Patient added successfully!")
            except ValueError:
                print("Invalid input. Please ensure age is a number.")

        # View Patients
        elif op == '2':
            print("-----List of Patients-----")
            if patients:
                #print('  ID |          Full Name       | Age |   Mobile     | Postcode |      Symptoms')
                print('  ID|          Full Name            |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms        ')
            for index, patient in enumerate(patients, start=1):
                print(f"{index:3} | {patient}")
            else:
                print("No patients registered.")

        # Update Patient
        elif op == '3':
            print("-----Update Patient Details-----")

            if not patients:
                print("No patients available to update.")
                return

            # Display list of patients
            print(' ID |          Full Name            |      Doctor`s Full Name      | Age |    Mobile     | Postcode |      Symptoms        ')
            for index, patient in enumerate(patients, start=1):
                print(f"{index:3} | {patient}")

            try:
                patient_index = int(input("Enter the ID of the patient to update: ")) - 1

                if 0 <= patient_index < len(patients):
                    selected_patient = patients[patient_index]

                    # Sub-menu for updating fields
                    print("Choose the field to update:")
                    print(" 1 - First Name")
                    print(" 2 - Surname")
                    print(" 3 - Age")
                    print(" 4 - Mobile Number")
                    print(" 5 - Postcode")
                    print(" 6 - Symptoms")

                    try:
                        field_option = int(input("Enter the option: "))

                        if field_option == 1:
                            new_first_name = input("Please Enter the new first name: ").strip()
                            selected_patient.set_first_name(new_first_name)
                        elif field_option == 2:
                            new_surname = input("Please Enter the new surname: ").strip()
                            selected_patient.set_surname(new_surname)
                        elif field_option == 3:
                            new_age = int(input("Please Enter the new age: ").strip())
                            selected_patient.set_age(new_age)
                        elif field_option == 4:
                            new_mobile = input("Please Enter the new mobile number: ").strip()
                            selected_patient.set_mobile(new_mobile)
                        elif field_option == 5:
                            new_postcode = input("Please Enter the new postcode: ").strip()
                            selected_patient.set_postcode(new_postcode)
                        elif field_option == 6:
                            new_symptoms = input("Please Enter new symptoms (comma-separated): ").split(',')
                            selected_patient.set_symptoms(new_symptoms)
                        else:
                            print("Invalid option selected. Please select a valid option.")

                        print("Patient details updated successfully!")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                else:
                    print("Invalid patient ID entered.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        else:
            print("Invalid operation selected. Please choose a valid option.")

    def group_patients_by_surname(self, patients):
        """
        Groups patients by their surname.

        Args:
            patients (list<Patient>): The list of all patients.

        Returns:
            dict: A dictionary where keys are surnames, and values are lists of patients with that surname.
        """

        print("-----Grouping Patients By Family (Surname)-----")
        grouped_patients = {}

        for patient in patients:
            surname = patient.get_surname()

            # Add the patient to the corresponding family group
            if surname in grouped_patients:
                grouped_patients[surname].append(patient)
            else:
                grouped_patients[surname] = [patient]

        # Display the grouped patients
        for surname, family_members in grouped_patients.items():
            print(f"Family: {surname}")
            for member in family_members:
                print(f" - {member.full_name()}")
            print()

        return grouped_patients

    def save_patient_data_to_file(self  ,patients,filepath = "patients_data.json"):
        try:
            patient_data = [
                {
                    "first_name": patient.get_first_name(),
                    "surname": patient.get_surname(),
                    "age": patient.get_age(),
                    "mobile": patient.get_mobile(),
                    "postcode": patient.get_postcode(),
                    "doctor": patient.get_doctor().full_name() if patient.get_doctor() != "None" else "None",
                    "symptoms": patient.get_symptoms()
                }
                for patient in patients
            ]
            with open(filepath, "w") as file:
                json.dump(patient_data, file, indent=4)
            print("Patient data has been saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving patient data: {e}")

    def load_patient_data_from_file(self,filepath = "patients_data.json"):
        try:
            with open(filepath,"r") as file:
                patient_data = json.load(file)
            patients = [
                Patient(
                    first_name=data["first_name"],
                    surname=data["surname"],
                    age=data["age"],
                    mobile=data["mobile"],
                    postcode=data["postcode"],
                    symptoms=data["symptoms"]
                )
                for data in patient_data
            ]
            print("Patient data has been loaded successfully.")
            return patients
        except FileNotFoundError:
            print("No saved Patient data found.")
            return []
        except Exception as e:
            print(f"An error occurred while loading patient data: {e}")
            return []

    def generate_management_report(self,doctors,patients, file_path = "management_report.pdf"):
        print("Generating management report...")
        diagrams = self.generate_view_diagrams(doctors, patients)
        total_doctors = len(doctors)  # Total number of doctors
        patients_per_doctor = {doc.full_name(): len(doc._Doctor__patients) for doc in doctors}  # Patients per doctor
        appointments_per_month = patients_per_doctor  # Assuming appointments = assigned patients
        illness_counts = Counter(
            symptom for patient in patients for symptom in patient.get_symptoms()
        )
        pdf = FPDF()
        pdf.set_auto_page_break(auto =True,margin = 15)
        pdf.add_page()
        pdf.set_font('Arial', size = 16)

        #Title
        pdf.set_font("Arial", size=20, style="B")
        pdf.cell(200,10,txt = "Hospital Management Report",ln =True,align = "C")
        pdf.ln(10)
        #Date
        pdf.set_font("Arial", size=16,)
        pdf.cell(200,10,txt = f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",ln =True,align = "C")
        pdf.ln(10)
        # Total Doctors
        pdf.set_font("Arial", style="B", size=18)
        pdf.cell(200, 10, txt="1. Total Number of Doctors", ln=True, align="L")
        pdf.set_font("Arial", size=16)
        pdf.cell(200, 10, txt=f"Total Doctors: {total_doctors}", ln=True, align="L")
        pdf.image(diagrams['total_doctors'], x=10, y=pdf.get_y() + 5, w=180)
        pdf.ln(10)
        # Patients Per Doctor
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=18)
        pdf.cell(200, 10, txt="2. Total Number of Patients Per Doctor", ln=True, align="L")
        pdf.set_font("Arial", size=16)
        for doctor, num_patients in patients_per_doctor.items():
            pdf.cell(200, 10, txt=f"{doctor}: {num_patients} patients", ln=True, align="L")
        pdf.ln(10)
        pdf.image(diagrams['patients_per_doctor'], x=10, y=pdf.get_y() + 5, w=180)
        pdf.ln(90)
        # Appointments Per Month
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=18)
        pdf.cell(200, 10, txt="3. Total Number of Appointments Per Month (Per Doctor)", ln=True, align="L")
        pdf.set_font("Arial", size=16)
        for doctor, num_appointments in appointments_per_month.items():
            pdf.cell(200, 10, txt=f"{doctor}: {num_appointments} appointments", ln=True, align="L")
        pdf.ln(10)
        pdf.image(diagrams['appointments_per_month'], x=10, y=pdf.get_y() + 5, w=180)
        pdf.ln(90)
        #Patients Based on Illness Type
        pdf.add_page()
        pdf.set_font("Arial", style="B", size=18)
        pdf.cell(200, 10, txt="4. Total Number of Patients Based on Illness Type", ln=True, align="L")
        pdf.set_font("Arial", size=16)
        for illness, count in illness_counts.items():
            pdf.cell(200, 10, txt=f"{illness}: {count} patients", ln=True, align="L")
        pdf.ln(10)
        pdf.image(diagrams['patients_per_illness'], x=10, y=pdf.get_y() + 5, w=180)
        pdf.ln(90)

        #Save PDF
        try:
            pdf.output(file_path)
            print(f"Management report generated successfully and Saved as {file_path}")
        except Exception as e:
            print(f"An error occurred while saving the management report: {e}")
            # Cleanup
        for path in diagrams.values():
            os.remove(path)

    def generate_view_diagrams(self,doctors,patients):
        diagram_paths = {}
        # (a) Total number of doctors (Bar Chart)
        plt.figure(figsize=(6, 4))
        total_doctors = len(doctors)
        plt.bar(['Total Doctors'], [total_doctors], color='teal')
        plt.title("Total Number of Doctors in the System")
        plt.ylabel("Count")
        total_doctors_path = 'total_doctors.png'
        plt.savefig(total_doctors_path, bbox_inches='tight')
        plt.close()
        diagram_paths['total_doctors'] = total_doctors_path

        # 2. Bar Chart: Patients per Doctor
        doctor_names = [doc.full_name() for doc in doctors]
        patients_per_doctor = [len(doc._Doctor__patients) for doc in doctors]

        plt.figure(figsize=(10, 6))
        plt.bar(doctor_names, patients_per_doctor, color='skyblue')
        plt.title('Total Number of Patients per Doctor')
        plt.xlabel('Doctor')
        plt.ylabel('Number of Patients')
        plt.xticks(rotation=45, ha="right")
        bar_chart_path = 'patients_per_doctor.png'
        plt.savefig(bar_chart_path, bbox_inches='tight')
        plt.close()
        diagram_paths['patients_per_doctor'] = bar_chart_path
        # (c) Total number of appointments per month per doctor (Bar Chart)
        # Assuming each patient assigned to a doctor is an appointment.
        appointments_per_doctor = patients_per_doctor  # Placeholder for simulation data.

        plt.figure(figsize=(10, 6))
        plt.bar(doctor_names, appointments_per_doctor, color='lightgreen')
        plt.title("Total Appointments Per Month Per Doctor")
        plt.xlabel("Doctor")
        plt.ylabel("Appointments")
        plt.xticks(rotation=45, ha="right")
        appointments_per_month_path = 'appointments_per_month_per_doctor.png'
        plt.savefig(appointments_per_month_path, bbox_inches='tight')
        plt.close()
        diagram_paths['appointments_per_month'] = appointments_per_month_path

        # (d) Total number of patients based on illness type (Pie Chart)
        illness_counts = Counter(symptom for patient in patients for symptom in patient.get_symptoms())
        illnesses, counts = zip(*illness_counts.items()) if illness_counts else ([], [])

        plt.figure(figsize=(8, 8))
        if illnesses:  # Avoid error when no illnesses exist
            plt.pie(counts, labels=illnesses, autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
        else:
            plt.text(0.5, 0.5, "No illnesses recorded", ha='center', va='center', fontsize=16)
        plt.title("Total Number of Patients Based on Illness Type")
        patients_per_illness_path = 'patients_per_illness.png'
        plt.savefig(patients_per_illness_path, bbox_inches='tight')
        plt.close()
        diagram_paths['patients_per_illness'] = patients_per_illness_path

        return diagram_paths

    def save_admin_details_to_file(self, filepath='admin_data.json'):
        try:
            admin_data = {
                'username': self.__username,
                'password': self.__password,
                'address': self.__address
            }
            with open(filepath, 'w') as file:
                json.dump(admin_data, file)
            print("Admin details saved successfully.")
        except Exception as e:
            print(f"An error occurred while saving admin details: {e}")

    @staticmethod
    def load_admin_details_from_file(filepath='admin_data.json'):
        try:
            with open(filepath, 'r') as file:
                admin_data = json.load(file)
            return Admin(
                username=admin_data['username'],
                password=admin_data['password'],
                address=admin_data.get('address', '')
            )
        except FileNotFoundError:
            print("No saved admin data found. Using default credentials.")
            return Admin('admin', '456', 'A1 1BC')
        except Exception as e:
            print(f"An error occurred while loading admin details: {e}")
            return Admin('admin', '456', 'A1 1BC')

    def update_details(self):
        """
        Allows the user to update and change username, password and address
        """

        print('Please Choose the field to be updated:')
        print(' 1 Update admin Username')
        print(' 2 Update admin Password')
        print(' 3 Update admin Address')
        try:
            op = int(input('Input: '))
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 3")
            return
        if op == 1:
            new_username = input('Please Enter the new username: ')
            if new_username:
                self.__username  = new_username
                print("Username updated successfully.")
            else:
                print("Invalid input.Username cannot be Empty")

        elif op == 2:
            password = input('Please Enter the new password: ')
            # validate the password
            if password == input('Please Enter the new password again: '):
                self.__password = password
                print("Password updated successfully.")
            else:
                print("Passwords do not match. Try Again.")

        elif op == 3:
            #ToDo15
            new_address = input('Please Enter the new address: ')
            if new_address:
                self.__address = new_address
                print("Address updated successfully.")
            else:
                print("Invalid input.Address cannot be Empty")

        else:
            print("Invalid option.Please choose 1,2 or 3.")

        self.save_admin_details_to_file()

