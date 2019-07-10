a=int(input())-1
l=list(map(int,input().split()))
li=l[::-1]
for j in range(a):
     print(li[j],end="->")
print(li[a])
