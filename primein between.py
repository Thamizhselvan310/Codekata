n , m =input().split()
n=int(n)
m=int(m)
for i in range(n+1,m):
	if i%2!=0 and i%3!=0 and i%5!=0 and i%7!=0:
		print(i,end=" ")
