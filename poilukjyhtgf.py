def toString(List): 

def permute(a,b,c): 
    if b==c: 
        print toString(a) 
    else: 
        for i in xrange(b,c+1): 
            a[b], a[i] = a[i], a[l] 
            permute(a, b+1,c) 
            a[l], a[i] = a[i], a[b]
  

string = "ABC"
n = len(string) 
a = list(string) 
permute(a, 0, n-1) 
