#Defining a class with encapsulation
class Payment:
    def __init__(self, price):
        # Private attribute to store the final_price
        self.__final_price = price + price * 0.07 # Adding 7% tax
    
    # Method to get the final price
    def get_final_price(self):
        # returns the final_price after tax
        return self.__final_price

# Creating an instance of Payment class with price 900
Laptop = Payment(900) 
print(Laptop.get_final_price())
