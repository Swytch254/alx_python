def raise_exception_msg(message=""):
    if type(message) == str:
        print(message)
    else:
        raise NameError
        