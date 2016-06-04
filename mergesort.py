
def merge(A, p, q, r):
    n1 = q-p+1
    n2=r-q

    L = [n1+1]
    R = [n2+1]

    for i in xrange(1,n1):
        L[i]=A[p+i-1]

    for j in xrange(1,n2):
        R[j]=A[q+j]
    i=1
    j=1
   
    for k in xrange(p,r):
        if L[i]<=R[j]:
            A[k]=L[i]
            i=i+1
        else:
            A[k]=R[j]
            j=j+1
# end of merge

def mergesort(A, p, r):
    q=(p+r)/2
    if p<r:
        mergesort(A,p,q)
        mergesort(A,q+1,r)
        merge(A,p,q,r)
#end of mergesort

A=[9,7,5,1,2]
mergesort(A,0,4)
print A
