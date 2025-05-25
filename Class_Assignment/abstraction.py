"""
An abstract class cannot be instantiated directly and serves as a blueprint \
for other classes. Abstract methods, declared within an abstract class, \
define a contract that subclasses must implement.
"""


# Importing necessary modules for creating an abstract base class
from abc import ABC, abstractmethod

# Defining an abstract base class called Planet
class Planet(ABC):

    # Abstract method that must be implemented by any subclass
    @abstractmethod
    def have_life(self):
        pass

    @abstractmethod
    def color(self):
        pass

# Create class Neptune that inherits from Planet
class Neptune(Planet):
    def __init__(self):
        self._life = True  
        self._color = "Blue"  

    # Implementation of the abstract method
    def have_life(self):
        return self._life

    def color(self):
        return self._color

if __name__ == "__main__":
    # Create an instance of Neptune
    neptune = Neptune()

    # Output
    print("Does Neptune have life?", neptune.have_life())
    print("Color of Neptune:", neptune.color())
