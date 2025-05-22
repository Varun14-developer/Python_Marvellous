def sum(num1, num2):
    result = 0
    result = num1 + num2
    return result

def difference(num1, num2):
    result = 0
    result = num1 - num2
    return result

def product(num1, num2):
    result = 0
    result = num1 * num2
    return result

def division(num1, num2):
    result = 0
    result = num1 / num2
    return result

def main():

    print("Enter the first number : ")
    value1 = int(input())

    print("Enter second number : ")
    value2 = int(input())

    ans = sum(value1, value2)
    print("Sum : ",ans)

    ans = difference(value1, value2)
    print("Difference : ",ans)

    ans = product(value1, value2)
    print("Product : ", ans)

    ans = division(value1, value2)
    print("Division : ", ans)


if __name__ == "__main__":
    main()