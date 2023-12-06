def print_matrix_integer(matrix=[[]]):
    if type(matrix) == str:
        print(matrix)
    else:
        for char in matrix:
            for digit in char:
                print("{:d}".format(digit), end="")
            print()
