## LAB ASSIGNMENT :- 9 ( WEEK 9 LAB ACTIVITY 1)
## NAME :- AMOGH DATH K A 
## STUDENT ID NUMBER :- 24168333


####################### TOPIC #######################
# CREATING A BUS CLASS AND ADDING SOME KEY OPERATIONS TO PERFORM SPECIFIC PRE-DETERMINED FUNCTIONS

## STARTING THE CODE ##
# This is our base class called Vehicle
class Vehicle:
    def __init__(self):
        self.state = "Not in use"  # Initialize with the vehicle not being used

    # Method to move the vehicle, currently does nothing
    def move(self):
        pass

    # Method to stop the vehicle, currently does nothing
    def stop(self):
        pass

# Subclass of Vehicle specifically for buses
class Bus(Vehicle):
    def __init__(self):
        super().__init__()  # Call the parent class (Vehicle) initializer
        self.route = ["New Street", "Bullring", "Moor Street", "BCU"]  # Define bus route
        self.current_stop_index = 0  # Start at the first stop

    # Method to return the bus route as a string
    def get_route(self):
        return "New Street - Bullring - Moor Street - BCU"

    # Method to move the bus to the next stop
    def move(self):
        # Check if there are more stops ahead
        if self.current_stop_index < len(self.route) - 1:
            previous_stop = self.route[self.current_stop_index]  # Get the current stop
            self.current_stop_index += 1  # Move to the next stop
            next_stop = self.route[self.current_stop_index]  # Get the next stop
            print(f"The bus was at {previous_stop} and is moving to {next_stop}.")
        else:
            print("I am finished for today!")  # When the bus has reached the final stop

    # Overridden method to stop the bus, with a message
    def stop(self):
        print("I am a non-stop bus.")

# Subclass of Vehicle specifically for cars
class Car(Vehicle):
    # Currently, Car class does not add new functionality to Vehicle class
    pass

# Example usage of Bus class
bus = Bus()  # Create a new Bus object
print(bus.get_route())  # Print the bus route
bus.move()  # Move the bus to the next stop
bus.move()  # Move the bus to the next stop
bus.move()  # Move the bus to the next stop
bus.move()  # Attempt to move to the next stop (route complete message)
bus.stop()  # Try to stop the bus (non-stop message)

## END OF THE CODE ##
