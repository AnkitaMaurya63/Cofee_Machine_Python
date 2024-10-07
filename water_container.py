# water_reservoir.py

class WaterContainer:
    def __init__(self, capacity): 
        
        self.capacity = capacity  # Max capacity of the container in ml
        self.current_level = capacity  # Current level of water, initialized as full

    def get_water(self, amount):
        #Dispenses water from the container.
        #Returns The amount of water dispensed, or 0 if not enough water is available.
        if self.current_level >= amount:
            self.current_level -= amount
            print(f"Dispensing {amount}ml of water.")
            return amount
        else:
            print(f"Not enough water! Only {self.current_level}ml left.")
            return 0
    
    def refill(self): 
        #Refills the water container to its maximum capacity
        self.current_level = self.capacity
        print("Water container refilled to maximum capacity.")
    
    def check_water_level(self): 
        #Returns the current water level in the container(in ml)
        return self.current_level
