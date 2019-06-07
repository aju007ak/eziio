import sys, string, math, itertools

# Get all permutations of [1, 2, 3]
s = input()
L = list(itertools.permutations(s))
L2 = []
for i in range(0,len(L)) :
    s2 = ''.join(list(L[i]))
    L2.append(s2)
L2.sort()
L3 = [L2[0]]
for i in range(0,len(L2)-1) :
    if L2[i] != L2[i+1] :
        L3.append(L2[i+1])
for i in range(0,len(L3)) :
    print(L3[i])
