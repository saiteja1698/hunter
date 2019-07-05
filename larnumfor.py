t = int(input())
s = list(map(int,input().split()))
s.sort(reverse=True)
l=0
for i in range(0,len(s)):
	l=l*10+s[i]
print(l)
