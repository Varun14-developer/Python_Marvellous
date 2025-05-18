
def Add(value1, value2):
    result = value1 + value2
    return result

def main():
    print("Enter first number :")
    no1 = int(input())

    print("Enter Second Number :")
    no2 = int(input())

    ans = Add(no1, no2)

    print("Addition is :", ans)




if __name__=='__main__':
    main()