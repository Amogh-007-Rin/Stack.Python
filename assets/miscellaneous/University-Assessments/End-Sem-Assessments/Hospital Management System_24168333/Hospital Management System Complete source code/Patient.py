
class Patient:
    """Patient class"""

    def __init__(self, first_name, surname, age, mobile, postcode,symptoms = None):
        """
        Args:
            first_name (string): First name
            surname (string): Surname
            age (int): Age
            mobile (string): the mobile number
            address (string): address
        """
        self.__first_name = first_name
        self.__surname = surname
        self.__age = age
        self.__mobile = mobile
        self.__postcode = postcode
        self.__doctor = 'None'
        self.__symptoms =  symptoms if symptoms else []

    
    def full_name(self) :
        """full name is first_name and surname"""
        return f"{self.__first_name} {self.__surname}"

    def get_first_name(self) :
        return self.__first_name
    def set_first_name(self, new_first_name):
        self.__first_name = new_first_name

    def set_surname(self, new_surname):
        self.__surname = new_surname

    def set_doctor(self, new_doctor):
        self.__doctor = new_doctor
    def set_age(self, new_age):
        self.__age = new_age
    def set_mobile(self, new_mobile):
        self.__mobile = new_mobile
    def set_postcode(self, new_postcode):
        self.__postcode = new_postcode
    def set_symptoms(self, new_symptoms):
        self.__symptoms = new_symptoms
    def get_surname(self) :
        return self.__surname

    def get_doctor(self) :
        return self.__doctor

    def get_age(self) :
        return self.__age

    def get_mobile(self) :
        return self.__mobile

    def get_postcode(self) :
        return self.__postcode

    def link(self, doctor):
        """Args: doctor(string): the doctor full name"""
        self.__doctor = doctor

    def add_symptom(self, symptom):
        """Adds a symptom to the patient's symptom list

        Args:
            symptom (string): The symptom to be added
        """
        self.__symptoms.append(symptom)

    def get_symptoms(self):
        return self.__symptoms

    def print_symptoms(self):
        """prints all the symptoms"""
        if self.__symptoms:
            print("Symptoms:")
            for symptom in self.__symptoms:
                print(f"- {symptom}")
        else:
            print("No symptoms recorded.")

    def __str__(self):
        doctor_name = self.__doctor if isinstance(self.__doctor, str) else self.__doctor.full_name()
        symptoms = ', '.join(self.__symptoms) if self.__symptoms else "None"
        return (
            f'{self.full_name():^30}|{doctor_name:^30}|{self.__age:^5}|'
            f'{self.__mobile:^15}|{self.__postcode:^10}|{symptoms:^30}'
        )
