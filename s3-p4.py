import sys,string
a,k=(input().split())
a,k=int(a),int(k)
C=[int(x) for x in input().split()]
for i in range(0,a-1):
    for j in range(i-1,a):
        if C[i]+C[j]==k:
          print('YES')
          sys.exit()
print('NO')           
