from sys import argv

def main():
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print("1 argument:\n"
              "{}: {}".format(len(argv)-1, argv[1]))
    else:
        print("{} arguments:".format(len(argv)-1))
        index = 1
        for input in range(1, len(argv)):
            print("{}: {}".format(index, argv[index]))
            index += 1

if __name__ == "__main__":
    main()