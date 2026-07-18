class Doctor:
    """A class that deals with the Doctor operations"""

    def __init__(self, first_name, surname, speciality):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            speciality (string): Doctor`s speciality
        """

        self.__first_name = first_name
        self.__surname = surname
        self.__speciality = speciality
        self.__patients = []
        self.__appointments = []

    
    def full_name(self) :
        #ToDo1
        return f"{self.__first_name} {self.__surname}"

    def get_first_name(self) :
        #ToDo2
        return self.__first_name

    def set_first_name(self, new_first_name):
        #ToDo3
        self.__first_name = new_first_name

    def get_surname(self) :
        #ToDo4
        return self.__surname

    def set_surname(self, new_surname):
        #ToDo5
        self.__surname = new_surname

    def get_speciality(self) :
        #ToDo6
        return self.__speciality

    def set_speciality(self, new_speciality):
        #ToDo7
        self.__speciality = new_speciality

    def add_patient(self, patient):
        self.__patients.append(patient)

    def view_assigned_patients(self):
        """Displays a list of all patients assigned to the doctor."""
        if not self.__patients:
            print(f"Dr. {self.full_name()} currently has no assigned patients.")
            return

        print(f"----- Patients Assigned to Dr. {self.full_name()} -----")
        print('ID  |     Full Name        | Age |   Mobile     | Postcode | Symptoms ' )
        for index, patient in enumerate(self.__patients, start=1):
            symptoms = ', '.join(patient.get_symptoms()) if patient.get_symptoms() else "None"
            print(f'{index:3} | {patient.full_name():<20} | {patient.get_age():<3} | {patient.get_mobile():<12} | {patient.get_postcode():<8} | {symptoms:<30}')
    def __str__(self) :
        return f'{self.full_name():^30}|{self.__speciality:^15}'
