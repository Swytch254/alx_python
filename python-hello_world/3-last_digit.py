import random
number = random.randint(-10000, 10000)
last_number = str(number)[-1]
if number > 0 and int(last_number) > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, last_number))
elif number < 0 and int(last_number) != 0:
    print("Last digit of {} is -{} and is less than 6 and not 0".format(number, last_number))
elif int(last_number) == 0:
    print("Last digit of {} is {} and is 0".format(number, last_number))
elif number > 0 and int(last_number) < 6 and int(last_number) != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number, last_number))
elif number > 0 and int(last_number) == 0:
    print("Last digit of {} is {} and is 0".format(number, last_number))
