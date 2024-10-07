# user_interface.py

class UserInterface:
    def __init__(self, coffee_machine):
        
        self.coffee_machine = coffee_machine
    
    def display_options(self):

        #Displays the options available to the user.

        print("\n--- Coffee Machine Menu ---")
        print("1. Make Espresso (Rs.100)")
        print("2. Make Latte (Rs.150)")
        print("3. Insert Rupees")
        print("4. Check Machine Status")
        print("5. Refill Machine Components")
        print("6. Get Refund")
        print("7. Exit\n")
    
    def get_user_input(self):
        
        try:
            choice = int(input("Choose an option: "))
            return choice
        except ValueError:
            print("Invalid input! Please enter a number.")
            return -1
    
    def run(self):
        #Runs the main loop of the user interface, allowing interaction with the coffee machine.
        while True:
            self.display_options()
            choice = self.get_user_input()
            
            if choice == 1:
               # Brew Espresso
                self.coffee_machine.brew_coffee('espresso')
            elif choice == 2:
                # Brew Latte
                self.coffee_machine.brew_coffee('latte')  
            elif choice == 3:
                 # Insert Coins
                amount = float(input("Insert Rupees (in INR): Rs."))
                self.coffee_machine.insert_coins(amount)
            elif choice == 4:
                # Check the current status of the machine
                self.coffee_machine.check_status()
            elif choice == 5:
                # Refill the machine components (water, beans, milk)
                self.coffee_machine.refill()
            elif choice == 6:
                # Refund any remaining balance
                self.coffee_machine.refund()
            elif choice == 7:
                # Exit the program
                print("Exiting the coffee machine. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
