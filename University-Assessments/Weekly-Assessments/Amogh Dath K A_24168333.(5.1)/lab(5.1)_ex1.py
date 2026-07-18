## LAB ASSIGNMENT :- 5.1
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333


####################### TOPIC #######################

# CREATING THE FOLLOWING FUNCTION ASKED IN THE MODULE TO SHOW SPECIFIC LIST AND ITS DATA IN DIFFERENT MANNER AS ASKED .

# Function to create the list
def create_list():
    return ['PlayStation', 'Xbox', 'Steam', 'iOS', 'Google Play']

# Function to get information from the list
def get_info(my_list):
    return (my_list[0], my_list[3], len(my_list))

# Function to get partial list
def get_partial(my_list):
    return my_list[1:4]

# Function to get the last three elements in reverse order
def get_last_three(my_list):
    return my_list[-3:][::-1]

# Function to double the list
def double_list(my_list):
    return my_list + my_list

# Function to amend the list
def amend(my_list):
    my_list[1] = 'None'
    my_list.append('Bye')
    return my_list

# Example usage
if __name__ == "__main__":
    my_list = create_list()
    print("Original list:", my_list)
    print("Info:", get_info(my_list))
    print("Partial list:", get_partial(my_list))
    print("Last three in reverse:", get_last_three(my_list))
    print("Doubled list:", double_list(my_list))
    print("Amended list:", amend(my_list))
