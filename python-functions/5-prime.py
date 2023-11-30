def is_prime(number):
    if number % 2 != 0 and number % 3 != 0 and number > 0:
        return True
    elif number == 2 or number == 3:
        return True
    else:
        return False
    