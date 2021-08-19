T= int(input())
while(T>0):
    i = int(input())
    rev = 0
    x = i  # x contains value of i

    while (i>0):
        rev = rev * 10 + i % 10       # i % 10 will print the last element of the number present in i
        i = i//10          # it will print the rest elements

    if(x==rev):
        print("Palindrome")
    else:
        print("Not Palindrom")



















