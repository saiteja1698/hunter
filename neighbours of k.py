a,b=map(int,input().split())
l=list(map(int,input().split()))
c=[]
s1=[[abs(i-b),i]for i in l]
s1=sorted(s1)
s1=s1[1:]
s1=[i[1] for i in s1[:3]]
print(*s1)
