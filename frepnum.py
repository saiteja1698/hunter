s = int(input())
e = list(map(int,input().split()))
e.sort()
b = []
for i in range(len(e)-1):
    if e[i]==e[i+1]:
        b.append(e[i])
        break
if b:
    for x in  set(b):
        print(x,end=" ")
else:
    print("unique")
