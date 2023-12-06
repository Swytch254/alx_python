def print_matrix_integer(matrix=[[]]):
    if type(matrix) == str:
        print("{}".format(matrix))
    else:
        for char in matrix:
            for digit in char:
                print("{} ".format(digit), end = "")
            print()
