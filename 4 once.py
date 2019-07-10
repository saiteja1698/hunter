n= int(input())
l=[z for z in input().split()]
l1=[]
for i in range(len(l)):
     if l[i] ==str(i):
       l1.append(l[i])
if len(l1) == 0:
  print('-1')
else:
   print(' '.join(sorted(l1)))
