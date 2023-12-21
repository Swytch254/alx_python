# Write a class Square that defines a square by:

#     Private instance attribute: size
#     Instantiation with size (no type/value verification)
# class definition
class Square:
    def __init__(self,size=0):
        self.__size = size                          #this creates a private instance attribute that cannot be called
