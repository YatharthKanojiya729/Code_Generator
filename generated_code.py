```python
class Vehicle:
    def __init__(self, vehicle_id, vehicle_type, fuel_type):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type
        self.fuel_type = fuel_type
        self.fuel_quantity = 0

    def add_fuel(self, quantity):
        self.fuel_quantity += quantity

    def remove_fuel(self, quantity):
        if self.fuel_quantity >= quantity:
            self.fuel_quantity -= quantity
        else:
            print("Insufficient fuel quantity.")

    def display_details(self):
        print(f"Vehicle ID: {self.vehicle_id}")
        print(f"Vehicle Type: {self.vehicle_type}")
        print(f"Fuel Type: {self.fuel_type}")
        print(f"Fuel Quantity: {self.fuel_quantity} units")


class PetrolPump:
    def __init__(self):
        self.vehicles = {}
        self.inventory = {"diesel": 1000, "petrol": 1000}

    def add_vehicle(self, vehicle_id, vehicle_type, fuel_type):
        if fuel_type in self.inventory:
            self.vehicles[vehicle_id] = Vehicle(vehicle_id, vehicle_type, fuel_type)
            print(f"Vehicle added successfully: {vehicle_id}")
        else:
            print("Fuel type not available in inventory.")

    def remove_vehicle(self, vehicle_id):
        if vehicle_id in self.vehicles:
            del self.vehicles[vehicle_id]
            print(f"Vehicle removed successfully: {vehicle_id}")
        else:
            print("Vehicle not found.")

    def add_fuel_to_inventory(self, fuel_type, quantity):
        if fuel_type in self.inventory:
            self.inventory[fuel_type] += quantity
            print(f"Fuel added to inventory successfully: {fuel_type} - {quantity} units")
        else:
            print("Fuel type not available in inventory.")

    def remove_fuel_from_inventory(self, fuel_type, quantity):
        if fuel_type in self.inventory:
            if self.inventory[fuel_type] >= quantity:
                self.inventory[fuel_type] -= quantity
                print(f"Fuel removed from inventory successfully: {fuel_type} - {quantity} units")
            else:
                print("Insufficient fuel quantity in inventory.")
        else:
            print("Fuel type not available in inventory.")

    def display_vehicle_details(self, vehicle_id):
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id].display_details()
        else:
            print("Vehicle not found.")

    def display_inventory(self):
        print("Inventory:")
        for fuel_type, quantity in self.inventory.items():
            print(f"{fuel_type}: {quantity} units")


# Create a petrol pump
petrol_pump = PetrolPump()

# Add vehicles
petrol_pump.add_vehicle("V1", "Car", "diesel")
petrol_pump.add_vehicle("V2", "Truck", "petrol")

# Add fuel to inventory
petrol_pump.add_fuel_to_inventory("diesel", 500)
petrol_pump.add_fuel_to_inventory("petrol", 750)

# Display vehicle details
petrol_pump.display_vehicle_details("V1")

# Add fuel to a vehicle
petrol_pump.vehicles["V1"].add_fuel(200)

# Display vehicle details after adding fuel
petrol_pump.display_vehicle_details("V1")

# Remove fuel from inventory
petrol_pump.remove_fuel_from_inventory("diesel", 200)

# Display inventory
petrol_pump.display_inventory()
```

This code defines two classes: `Vehicle` and `PetrolPump`. The `Vehicle` class represents a vehicle with attributes like vehicle ID, type, fuel type, and fuel quantity. The `PetrolPump` class represents a petrol pump with methods to add and remove vehicles, add and remove fuel from the inventory, and display vehicle details and inventory.