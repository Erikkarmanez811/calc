import compare
def search(ar,n,comp):
    if len(ar) == 0: 
        return [False, -2]
    
    if len(ar) == 1:
        if ar[0] == n:
            return [True, 0]
        if comp(ar[0],n):
            return [False, 0]
        return [False, 1]
    
    if n == ar[len(ar)//2]:
        return [True, len(ar)//2]
    
    if comp(n,ar[len(ar)//2]):
        value = search(ar[len(ar)//2+1:],n,comp)
        if value[1] == -2:
            return [False,len(ar)]
        return [value[0], len(ar)//2+value[1]+1]  
    
    if comp(ar[len(ar)//2],n):
        return search(ar[:len(ar)//2],n,comp)
