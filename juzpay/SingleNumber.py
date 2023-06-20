def SingleNumber(n,a):
    for i in n:
        if(n.count(i)==1):
            x=i
            break
    return i



a=int(input())
n=list(map(int, input().split()))
n =[2,2,3,2]
print(SingleNumber(n,a))

