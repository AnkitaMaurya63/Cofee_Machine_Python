# money_system.py

class MoneySystem:
    def __init__(self): 
        #Initializes the MoneySystem with no money inserted.
        self.balance = 0.0  # Money inserted by the customer in INR

    def insert_coins(self, amount): # Inserts money (in rupees) into the machine.
        self.balance += amount
        print(f"You inserted Rs.{amount:.2f}. Current balance: Rs.{self.balance:.2f}")

    def process_payment(self, cost):
        #Processes the payment for the coffee.
        #Returns True if the payment is successful, False if not enough money is inserted.
        if self.balance >= cost:
            change = self.balance - cost
            self.balance = 0  # Reset balance after transaction
            if change > 0:
                print(f"Payment successful! Your change is Rs.{change:.2f}")
            else:
                print("Payment successful!")
            return True
        else:
            print(f"Not enough money! Coffee costs Rs.{cost:.2f}, but you have only Rs.{self.balance:.2f}")
            return False

    def refund(self): 
        #Refunds the current balance to the customer.
        if self.balance > 0:
            print(f"Refunding Rs.{self.balance:.2f}.")
            self.balance = 0
        else:
            print("No money to refund.")
