def main():

    def ChkNum(no1):
        if no1 % 2 == 0:
            print("Even Number")
        else:
            print("Odd Number")


    print("Enter a Number : ")
    value1 = int(input())

    result = ChkNum(value1)

if __name__ == "__main__":
    main()