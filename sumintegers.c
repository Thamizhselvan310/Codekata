#include<stdio.h>
void main()
{
int n,k,a[50],sum=0;
scanf("%d %d",&n,&k);
for(int i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(int i=0;i<k;i++)
{
sum=sum+a[i];
}
printf("%d",sum);
}
