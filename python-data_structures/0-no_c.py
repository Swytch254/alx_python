def no_c(my_string):
    string = my_string.lower()
    new_string = ""
    for char in string:
        if char != "c":
            new_string += char
    return new_string
