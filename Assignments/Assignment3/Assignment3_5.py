
def Addition(data):
    iSum = 0

    if(len(data)==0):
        return 0
    
    for i in range(0,len(data)):
        iSum +=data[i]

    return iSum

def ChkPrime(iNo):
    iRet = True
    
    counter  = (int)(iNo/2 + 1)

    for i in range(2,counter):
        if(iNo%i==0):
            iRet = False

    return iRet



def main():
    print("Enter the size :")
    iSize = int(input())

    data = list()
    print("Enter into List :")
    for i in range(0,iSize):
        value = int(input())
        ibool = ChkPrime(value)
        if(ibool):
            data.append(value)
    
    iRet = Addition(data)
    print(iRet) 

if __name__ == "__main__":
    main()