def search(ar,n):
    if len(ar) in [0,1]:
        if ar == []:
            return -2
        if ar[0] >= n:
            return 0
        return 1
    if n == ar[len(ar)//2]:
        return len(ar)//2
    if n > ar[len(ar)//2]:
        beer = search(ar[len(ar)//2+1:],n)
        if beer == -2:
            return len(ar)
            
        return len(ar)//2+1+ beer
    if n < ar[len(ar)//2]:
        return search(ar[:len(ar)//2],n)
while True:
    raw_a =list( map(int,input().split()))
    n = int(input())
    print(search(raw_a,n))  
