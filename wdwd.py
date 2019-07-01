import sys,string, itertools
def prod1(L) :
    p = 1
    for i in range(0,len(L)) :
        p *= L[i]
    return p

a = int(input())
L = [ int(x) for x in input().split()]
pr2 = prod1(L)

for j in range(a-2,-1,-1) :
    #print('arr len = ', j+1)
    for i in range(0,a-j) :
        li, ri = i,j+i
        pr1 = prod1(L[li:ri+1])
        #print(li, ri, pr1)
        if pr1 > pr2 :
            pr2 = pr1
print(pr2)
