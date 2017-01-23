def search(ar,n):
    if len(ar) in [0,1]:
        if ar == []:
            return -2
        if ar[0] != n:
            value = ar[0]
            return -1
    if n == ar[len(ar)//2]:
        return len(ar)//2
    if n > ar[len(ar)//2]:
        beer = search(ar[len(ar)//2+1:],n)
        if beer == -2:
            return len(ar)
        if beer == -1:
            if n == value:
                return ar[value]
            if n > value:
                return len(value)
            if n < value:
                return len(value) - 1
            
        return len(ar)//2+1+ beer
    if n < ar[len(ar)//2]:
        return search(ar[:len(ar)//2],n)
while True:
    raw_a =list( map(int,input().split()))
    n = int(input())
    print(search(raw_a,n))  
