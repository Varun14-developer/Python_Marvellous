def Add(iNo1,iNo2):
    return iNo1 + iNo2

def Sub(iNo1,iNo2):
    return iNo1 - iNo2


def Mul(iNo1,iNo2):
    return iNo1 * iNo2

def Div(iNo1,iNo2):
    return iNo1 / iNo2


def main():
    print("Enter the first number : ")
    iNo1 = int(input())
    print("Enter the second number : ")
    iNo2 = int(input())

    iSum = Add(iNo1,iNo2)
    iSub = Sub(iNo1,iNo2)
    iMul = Mul(iNo1,iNo2)
    iDiv = (iNo1,iNo2)

    print("Sum is :",iSum)
    print("Subtraction is :",iSub)
    print("Mulitpication  is  :",iMul)
    print("Division is :",Div(iNo1,iNo2))
if __name__ == "__main__":
    main()