n,m=input().split()
n1,m1=input().split()
n=int(n)
m=int(m)
n1=int(n1)
m1=int(m1)
b=(60*n)+m
c=(60*n1)+m1
result=b-c
t=result//60
m=result%60
print(t,m)
