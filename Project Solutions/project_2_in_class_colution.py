class Vehicle:
    vehicle_count = 0

    def __init__(self, make, year, availability):
        self.make = make
        self.year = year
        self.availability = availability
        Vehicle.vehicle_count += 1 

class Car(Vehicle):
    car_count = 0

    def __init__(self, make, year, availability, body_type, number_of_doors):
        super().__init__(make, year, availability)
        self.body_type = body_type
        self.number_of_doors = int(number_of_doors)
        Car.car_count += 1
    
    @classmethod
    def from_string(cls, car_info):
        make, year, availability, body_type, number_of_doors = car_info.split(",")
        return cls(make, year, availability, body_type, number_of_doors)

    @staticmethod
    def display_cars(list_of_cars):
        for this_car in list_of_cars:
            print(f"{this_car.year} {this_car.make} {this_car.body_type} with {this_car.number_of_doors} doors. Available: {this_car.availability}.")

class Motorcycle(Vehicle):
    motorcycle_count = 0

    def __init__(self, make, year, availability, has_sidecar):
        super().__init__(make, year, availability)
        self.has_sidecar = has_sidecar
        Motorcycle.motorcycle_count += 1
    
    @classmethod
    def from_string(cls, motorcycle_info):
        make, year, availability, has_sidecar = motorcycle_info.split(",")
        return cls(make, year, availability, has_sidecar)

    @staticmethod
    def display_motorcycles(list_of_motorcycles):
        for this_motorcycle in list_of_motorcycles:
            if this_motorcycle.has_sidecar:
                print(f"{this_motorcycle.year} {this_motorcycle.make} motorcycle with a sidecar. Available: {this_motorcycle.availability}.")
            else:
                print(f"{this_motorcycle.year} {this_motorcycle.make} motorcycle without a sidecar. Available: {this_motorcycle.availability}.")

def main():

    car_1 = Car("Ford", "2025", True, "Sedan", 4)
    car_2 = Car("GMC", "2023", True, "SUV", 4)
    list_of_cars = [car_1, car_2]

    mot_1 = Motorcycle("Yamaha", "2024", True, False)
    mot_2 = Motorcycle("Harley-Davidson", "2025", False, True)
    list_of_motorcycles = [mot_1, mot_2]

    while(True):
        answer = int(input("\nPlease choose one of the following options: \n" \
            "1. See the list of all cars.\n" \
            "2. See the list of all motorcycles.\n"
            "3. Add a new vehicle.\n"
            "4. See the count of every type of vehicle. \n"))
        if answer == 1:
            Car.display_cars(list_of_cars)
        elif answer == 2:
            Motorcycle.display_motorcycles(list_of_motorcycles)
        elif answer == 3:
            answer_2 = int(input("Choose 1 for car and 2 for motorcycle."))
            if answer_2 == 1:
                new_car_input = input("Enter the car's details separated by a comma.")
                new_car = Car.from_string(new_car_input)
                list_of_cars.append(new_car)
            elif answer_2 == 2: 
                new_motorcycle_input = input("Enter the motorcycle's details separated by a comma: \n")
                new_motorcycle = Motorcycle.from_string(new_motorcycle_input)
                list_of_motorcycles.append(new_motorcycle)
            else:
                print("Invalid input.")
        elif answer == 4:
            print(f"There are {Vehicle.vehicle_count} vehicles in total: {Car.car_count} are cars and {Motorcycle.motorcycle_count} are motorcycles.")
        else: 
            print("Invalid input.")

main()