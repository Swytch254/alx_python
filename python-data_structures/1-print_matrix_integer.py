def print_matrix_integer(matrix=[[]]):
    if type(matrix) == str:
        print("{}".format(matrix))
    else:
        for char in matrix:
            for digit in char:
                print("{:d} ".format(digit), end = "")
            print("{}".format(""))

# print_matrix_integer([[1,2,3],[4,5,6],[6,7,8]])