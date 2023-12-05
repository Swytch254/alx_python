def main():
    a = int(input())
    b = int(input())
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
