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
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size  

    
    def area(self):
        """
            A function to square the size
        """
        return self.__size * self.__size
    