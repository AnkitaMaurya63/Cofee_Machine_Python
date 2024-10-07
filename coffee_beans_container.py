class CoffeeBeansContainer:
    def __init__(self, capacity): 
        
        self.capacity = capacity  # Max capacity of the beans container in grams
        self.current_level = capacity  # Current level of beans, initialized as full

    def grind_beans(self, amount): # Grinds the required amount of coffee beans.
        if self.current_level >= amount:
            self.current_level -= amount
            print(f"Grinding {amount}g of coffee beans.")
            return True
        else:
            print(f"Not enough coffee beans! Only {self.current_level}g left.")
            return False

    def refill(self): 
        # Refills the coffee beans container to its maximum capacity.
        self.current_level = self.capacity
        print("Coffee beans container refilled to maximum capacity.")
    
    def check_bean_level(self): 
        # Returns the current coffee bean level in the container(in grams).
        return self.current_level
