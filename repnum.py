s = int(input())
t = list(map(int,input().split()))
t.sort()
j = []
for i in range(len(t)-1):
    if t[i]==t[i+1]:
        j.append(t[i])
if j:
    for x in set(j):
        print(x,end=" ")
else:
    print("unique")
