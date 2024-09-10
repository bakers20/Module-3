# Superclass Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Subclass Automobile inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self, year, make, model, doors, roof):
        super().__init__('car')  # Vehicle type is always 'car' for this app
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    def display_info(self):
        # Displaying car information in a formatted way
        print(f"Vehicle type: {self.vehicle_type}")
        print(f"Year: {self.year}")
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Number of doors: {self.doors}")
        print(f"Type of roof: {self.roof}")

# Function to get input from the user and create an Automobile object
def get_car_info():
    year = input("Enter the year of the car: ")
    make = input("Enter the make of the car: ")
    model = input("Enter the model of the car: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Creating an Automobile object with the user inputs
    car = Automobile(year, make, model, doors, roof)
    return car

# Main function
if __name__ == "__main__":
    car = get_car_info()
    car.display_info()
