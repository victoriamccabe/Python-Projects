class User:
    # Define the attibutes of the class
    fName = ''
    lName = ''
    phone = ''
    
    #Define methos of the class
    def login(self):
        entry_fName = input("Please provide your first name: ")
        entry_lName = input("Please provide your last name: ")

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
                
# Instance of the User class
new_user = User()
# Call the login method using the new object
new_user.login()


class Patient(User):
    MRN = ''

class Provider(User):
    License_number = ''
