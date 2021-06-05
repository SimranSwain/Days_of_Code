l=list(input().split(" "))
a=int(l[0])
b=int(l[1])

if a<b:
    print("{} is smaller than {}" .format(a,b))
elif a>b:
    print("{} is greater than {}" .format(a,b))
else:
    print("{} '=' {}" .format(a,b))