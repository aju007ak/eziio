import sys, string, math, itertools
def isprime(n) :
    if n == 1 : return False
    if n == 2: return True
    for i in range(2,n) :
        if n%i == 0 : return False
    return True

a,b = input().split()
a = int(a)
b = int(b)
cnt = 0
for i in range(a,b+1) :
    s = bin(i)[2:]
    k = s.count('1')
    if isprime(k) : cnt += 1
print(cnt)
