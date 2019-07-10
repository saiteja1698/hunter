n=input()
l=list(map(int,input().split()))
for j in range(len(l)):
  if (j%2 == 0 and l[j]%2 !=0) or (j%2!= 0 and l[j]%2 == 0):
    print(l[j],end=" ")

