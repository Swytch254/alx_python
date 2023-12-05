def main():
    a = 2
    b = 1
    safe_print_division(a,b)

def safe_print_division(a,b):
    try:
        result = a/b
    except (ValueError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}\n".format(result), end = "")
        print("{} / {} = {}".format(a,b,result))
        
if __name__ == "__main__":
    main()
    