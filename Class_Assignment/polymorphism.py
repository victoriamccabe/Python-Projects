# Define the User class
class User:
    # The init method runs when you create a new User object
    def __init__(self, fName, lName, phone):

        #'self' refers to the current object
        self.fName = fName  
        self.lName = lName   
        self.phone = phone     
    
    #Define method of the class
    def login(self):
        # Added .lower() method to convert user input to lower case.
        entry_fName = input("Please provide your first name: ").lower()
        entry_lName = input("Please provide your last name: ").lower()

        # Start a loop until valid input is received
        while True:
            entry_phone = input("Enter your phone number: ")
            # Check if the input contains only digits 10 characters long
            if entry_phone.isdigit() and len(entry_phone) == 10:
                # If valid, break out of the loop
                break
            else:
                print("Please enter 10 digits phone number only.")

        if (entry_lName == self.lName and entry_phone == self.phone):
            print("Welcome back, {} {}".format(self.fName,self.lName))
        else:
            print("Oops!, user not found.")



"""

Subclasses: 
Define Patient class, which is a type of User

"""
# Subclass Patient (inherits from User) added ssn_last4
class Patient(User):
    def __init__(self, fName, lName, phone, ssn_last4):
        super().__init__(fName, lName, phone)
        self.ssn_last4 = ssn_last4

    # Overriding login method -- (polymorphism)
    def login(self):
        entry_fName = input("Please provide your first name: ").lower()
        entry_lName = input("Please provide your last name: ").lower()

        while True:
            entry_ssn = input("Enter the last 4 of your SSN: ")
            if entry_ssn.isdigit() and len(entry_ssn) == 4:
                break
            else:
                print("Enter the last 4 digits of your SSN only.")

        if entry_lName == self.lName and entry_ssn == self.ssn_last4:
            print("Welcome back, {} {}".format(self.fName, self.lName))
        else:
            print("Oops! Patient not found.")


# Define the class, which inherits from the User class
class Provider(User):
    def __init__(self, fName, lName, phone, license_number):
        # Call the parent class's __init__ method to set fName, lName, and phone
        # and prevents us from rewriting the same initialization code
        super().__init__(fName, lName, phone)
        # Add license number specific to Provider
        self.license_number = license_number

    # Overriding login method -- (polymorphism)
    def login(self):
        entry_fName = input("Please provide your first name: ").lower()
        entry_lName = input("Please provide your last name: ").lower()
        entry_license = input("Enter your license number: ")

        if entry_lName == self.lName and entry_license == self.license_number:
            print("Welcome back, {} {}".format(self.fName, self.lName))
        else:
            print("Oops! Patient not found.")    


if __name__ == "__main__":
    print("---- Testing User Login ----")
    user1 = User("lilly", "moe", "0123456789")
    user2 = Provider("monica","pampa","1234567890","12345")
    
    user2.login()
