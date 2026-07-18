## LAB ASSIGNMENT :- 8.2( WEEK 8 LAB ACTIVITY 2 )
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333


####################### TOPIC #######################

## some small upgradation for BMI calculator ##

class BMI:
    def __init__(self):
        # Initial weight and height are set to 0.0
        self.weight = 0.0
        self.height = 0.0

    def set_weight(self, weight):
        # Set the weight value
        self.weight = weight

    def set_height(self, height):
        # Set the height value
        self.height = height

    def __calculate_bmi(self):
        # Calculate BMI, making sure height is not zero
        if self.height == 0:
            return 0
        return self.weight / (self.height ** 2)

    def display_bmi(self):
        # Calculate and print BMI with two decimal places
        bmi = self.__calculate_bmi()
        print(f"BMI is {bmi:.2f}")

# Example of how to use the class
if __name__ == "__main__":
    my_bmi = BMI()
    my_bmi.set_weight(55)   # Set weight to 55 kg
    my_bmi.set_height(1.70) # Set height to 1.70 meters
    my_bmi.display_bmi()    # Display the calculated BMI

## the result of this BMI calculation is show as 19.03 when height = 1.70m and weight = 55kg . also there will be a multiple range of height and weights which will give the same BMI of 19.03.
## few more combinations of height and weight to get the same BMI value of 19.03.
# Height: 1.75 meters and Weight: 58.3 kg
# Height: 1.60 meters and Weight: 48.7 kg
# Height: 1.70 meters and Weight: 54.9 kg
# Height: 1.80 meters and Weight: 61.6 kg
# Height: 1.90 meters and Weight: 68.6 kg
# Height: 2.00 meters and Weight: 76.1 kg
