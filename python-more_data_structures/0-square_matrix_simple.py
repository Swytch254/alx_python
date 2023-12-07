def square_matrix_simple(matrix): 
    new_matrix = []
    for char in matrix:
        char_list = []
        for digit in char:
            char_list.append(digit * digit)
        new_matrix.append(char_list)
    return new_matrix
