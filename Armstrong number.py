i = int(input())
orig = i
sum = 0

while(i>0):
    sum = sum + (i%10)*(i%10)*(i%10)
    i = i//10

if (sum==orig):
    print("Armstrong no.")
else:
    print("Not a Armstrong no.")