X=int(input())
sum=0
while(X>0):
  sum=sum+X%10
  X=X//10
print(sum)