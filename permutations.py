from itertools import permutations
c=input()
d=permutations(c)
for j in list(d):
    print("".join(j))
