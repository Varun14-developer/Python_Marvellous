def main():

    def Num(no1):
        if no1 > 0:
            print("Positive Number")

        elif no1 < 0:
            print("Negative Number")

        else:
            print("Zero")

    print("Enter a Number :")
    value = int(input())

    result = Num(value)


if __name__ == "__main__":
    main()