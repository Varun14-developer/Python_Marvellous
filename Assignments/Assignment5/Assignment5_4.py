def main():

    print("Enter the first number :")
    num1 = int(input())

    print("Enter second number :")
    num2 = int(input())

    print("Enter third number :")
    num3 = int(input())

    if num1 > num2:
        if num1 > num3:
            print("Largest number is :", num1)
        else:
            print("Largest number is :", num3)
    else:
        if num2 > num3:
            print("Largest number is :", num2)
        else:
            print("Largest number is ", num3)
                

if __name__ == "__main__":
    main()