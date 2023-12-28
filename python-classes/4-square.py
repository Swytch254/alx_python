"""
    Square with size

"""

class Square:                                       
    """
        A class used to represent the Square class

    """
    def __init__(self,size=0):
        """
            Initializes the instance 
            Parameters
            ----------
            size : no type, optional
                private instance attribute, the size of the square(default is 0)
            raises :
                TypeError : if size is not an integer
                ValueError : if size is less than 0
        """                        
        self.size = size


    @property
    def size(self):
        """
            A getter function for the Square class that has the size attribute
        """
        return self.__size
    

    @size.setter
    def size(self, value):
        """
            A setter function for getting the value of size
        """
        if not isinstance(value,int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value 


    def area(self):
        """
            A function to square the size
        """
        if not isinstance(self.size,int):
            raise TypeError("size must be an integer")
        elif self.size < 0:
            raise ValueError("size must be >= 0")
        return self.size * self.size


    def my_print(self):
        """
            A function to print in stdout the square with the character #
        """
        if self.size == 0:
            print()
            print()
