# Python:   3.11.7
#
# Author:   Daniel A Christie
#
# Purpose:  The Tech Academy - Python Course, Creating our first program together.
#           Demostrating how to pass variables from function to function
#           while producing a functional game.
#       
#           Remember, function_name(variable) _means that we pass in the variable.
#           return varibale _means thatg we are returning the variable to 
#           back to the calling function.


def start():
    print("Hello {}!".format (get_name()))


def get_name():
    name = input("What is your name?: ")
    return name


if __name__ == "__main__":
    start()


