n=int(input())
n1=set(map(int,input().split()))
m=int(input())
m1=set(map(int,input().split()))
ans=n1.intersection(m1)
count=0
for i in ans:
    count=count+1
print(count)