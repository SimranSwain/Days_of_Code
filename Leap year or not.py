def getLeafyear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("Yes")
            else:
                print("No")
        else:
            print("Yes")
    else:
        print("No")

if __name__=='__main__':
    getLeafyear(int(input()))