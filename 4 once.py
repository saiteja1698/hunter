n= int(input())
l=list(map(int,input().split()))
m=[]
for i in l:
     if l.count(i) ==1:
       if i not in m:
          m.append(i)
for j in m:
    print(j,end= " ")    

