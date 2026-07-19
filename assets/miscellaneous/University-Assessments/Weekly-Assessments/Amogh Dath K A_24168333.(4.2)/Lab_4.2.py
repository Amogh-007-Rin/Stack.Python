## LAB ASSIGNMENT :- 4.2
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333

#################################################################################### TOPIC ####################################################################################
                                                                ####  Designing a program which generates housing occupancy report ####
 #1. In this task, you will design a program which display a census report of the numbers and percentages of houses with particular numbers of occupants in a road. 
 #2. When the program starts, it should ask the user 8 times about houses with occupancy of 0 to 6, plus 6+ to count the numbers of houses with particular numbers of occupants.
 #3. After user entered the data, the program will calculate the percentage of each occupancy category. 

def get_data():
    # Function to get occupancy data from user
    occupancies = []
    for i in range(7):
        occupants = int(input(f"Enter the number of houses with {i} occupants: "))
        occupancies.append(occupants)
    more_than_six = int(input("Enter the number of houses with more than 6 occupants: "))
    occupancies.append(more_than_six)
    return occupancies

def cal_percentage(occupancy_list):
    # Function to calculate percentages
    total_houses = sum(occupancy_list)
    percentages = []
    for count in occupancy_list:
        if total_houses > 0:
            percentage = (count / total_houses) * 100
        else:
            percentage = 0
        percentages.append(percentage)
    return percentages

def display_result(occupancies, percentages):
    # Function to display the result
    print("\nHousing Occupancy Report")
    print("{:<20} {:<20} {:<20}".format("Occupancy", "Number of Houses", "Percentage"))
    for i in range(7):
        print("{:<20} {:<20} {:<20}".format(f"{i} occupants", occupancies[i], f"{percentages[i]:.2f}%"))
    print("{:<20} {:<20} {:<20}".format("More than 6 occupants ", occupancies[7], f"{percentages[7]:.2f}%"))

def main():
    # Main function to run the program
    occupancies = get_data()
    percentages = cal_percentage(occupancies)
    display_result(occupancies, percentages)

# Run the program
if __name__ == "__main__":
    main()
## following is the modifications of given empty skeliton code and the result will be displayed in the terminal ##