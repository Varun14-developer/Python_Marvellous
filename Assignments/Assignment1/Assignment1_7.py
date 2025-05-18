def main():

    def Num(no):
        if no % 5 == 0:
            print("True")

        else:
            print("False")

    print("Enter a Number : ")
    value = int(input())

    result = Num(value)


if __name__ == "__main__":
    main()