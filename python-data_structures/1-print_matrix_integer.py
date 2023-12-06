def print_matrix_integer(matrix=[[]]):
    if type(matrix) == str:
        print(matrix)
    else:
        formatted_matrix = []
        for char in matrix:
            formatted_row = []
            for digit in char:
                formatted_row.append("{:d}".format(digit))
            formatted_matrix.append(" ".join(formatted_row))
        print("\n".join(formatted_matrix))
