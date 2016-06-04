def insertionsort(A):
    for i in xrange (1,len(A)):
        key = A[i]
        k = i-1
        while(k>=0 and A[k]>key):
            A[k+1]=A[k]
            k=k-1
        A[k+1]=key

A = [8,0,6,10,98,7]
insertionsort(A)
print A
print len(A)
print A[6]
