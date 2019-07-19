a,b=input().split()
a=int(a)
b=int(b)
for num1 in range(a,b):
  sum=0
  temp=num1
  while(temp>0):
     digit=temp%10
     sum+=digit**3
     temp=temp//10
  if(sum==num1):
     print(num1,end=" ")
