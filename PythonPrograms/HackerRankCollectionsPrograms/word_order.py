from collections import Counter
n=int(input())
l=[]
for i in range(n):
    l.append(input())
c=Counter(l)
print(len(c))
for i in c.values():
    print(i,end=' ')