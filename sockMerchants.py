def sockMerchant(n,arr)
    count=0
    m=[x for x in arr if arr.count(x)>=2]
    raj={}
    for i in m:
        if i in raj:
            raj[i]+=1
        else:
            raj[i]=1
    for i in raj:
        count+=int(raj[i]/2)
    return count
n=int(input())
arr=list(map(int,input().split()))
print(sockMerchant(n,arr)