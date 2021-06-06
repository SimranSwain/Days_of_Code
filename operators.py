l=list(input().split(" "))
a=int(l[0])
b=int(l[1])

if a<b:
    print(f"{a} is smaller than {b}")
elif a>b:
    print(f"{a} is greater than {b}")
else:
    print(f"{a} '=' {b}")