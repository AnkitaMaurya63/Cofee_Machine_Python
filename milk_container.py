class MilkContainer:
    def __init__(self, capacity): 
        
        self.capacity = capacity  # Max capacity of the milk Container in ml
        self.current_level = capacity  # Current level of milk, initialized as full

    def use_milk(self, amount):
        #Dispenses milk from the container.
        #Returns True if enough milk is available, False if not enough milk is available.
        if self.current_level >= amount:
            self.current_level -= amount
            print(f"Dispensing {amount}ml of milk.")
            return True
        else:
            print(f"Not enough milk! Only {self.current_level}ml left.")
            return False

    def refill(self): 
        # Refills the milk container to its maximum capacity.
        self.current_level = self.capacity
        print("Milk container refilled to maximum capacity.")
    
    def check_milk_level(self): 
        # Returns the current milk level in the container(in ml)
        return self.current_level
