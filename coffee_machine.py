from money_system import MoneySystem
from water_container import WaterContainer
from coffee_beans_container import CoffeeBeansContainer
from milk_container import MilkContainer
from user_interface import UserInterface

class CoffeeMachine:
    def __init__(self):
        
        #Initializes the CoffeeMachine with its components and pricing in INR.
        self.water_container = WaterContainer(1000)  # 1000ml capacity
        self.beans_container = CoffeeBeansContainer(500)  # 500g capacity
        self.milk_container = MilkContainer(300)  # 300ml capacity
        self.money_system = MoneySystem()  # Initialize money system

        # Coffee prices in INR
        self.prices = {
            'espresso': 100,  # ₹100 for espresso
            'latte': 150      # ₹150 for latte
        }
    
    def brew_coffee(self, coffee_type): #Brews coffee if the customer has inserted enough money (in INR).
        if coffee_type not in self.prices:
            print(f"Sorry, {coffee_type} is not available.")
            return

        # Check if enough money has been inserted
        coffee_cost = self.prices[coffee_type]
        if self.money_system.process_payment(coffee_cost):
            # Brew coffee if payment is successful
            if coffee_type == 'espresso':
                water_needed = 50
                beans_needed = 20
                if self.water_container.get_water(water_needed) and \
                   self.beans_container.grind_beans(beans_needed):
                    print("Your espresso is ready!")
            elif coffee_type == 'latte':
                water_needed = 50
                beans_needed = 20
                milk_needed = 50
                if self.water_container.get_water(water_needed) and \
                   self.beans_container.grind_beans(beans_needed) and \
                   self.milk_container.use_milk(milk_needed):
                    print("Your latte is ready!")
    
    def check_status(self): #Prints the current status of the coffee machine's components.
        print("Water level:", self.water_container.current_level, "ml")
        print("Beans level:", self.beans_container.current_level, "g")
        print("Milk level:", self.milk_container.current_level, "ml")
    
    def refill(self): #Refills the water, beans, and milk components of the coffee machine.
        self.water_container.refill()
        self.beans_container.refill()
        self.milk_container.refill()

    def insert_coins(self, amount): #Insert money into the coffee machine (in INR).
        self.money_system.insert_coins(amount)
    
    def refund(self): # Refunds any money inserted.
        self.money_system.refund()
def main():
    coffee_machine = CoffeeMachine()
    user_interface = UserInterface(coffee_machine)
    user_interface.run()

if __name__ == "__main__":
    main()