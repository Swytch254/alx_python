def main():
    a = int(input())
    b = int(input())
    result = safe_print_division(a,b)
    print("{} / {} = {}".format(a,b,result))

def safe_print_division(a,b):
    try:
        result = a/b
    except (ValueError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}\n".format(result), end = "")
        return result
        
if __name__ == "__main__":
    main()
