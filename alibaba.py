
def divideList(alist):
    if len(alist)<=4:
        return False
    left = 1
    right = len(alist)-2
    while left<right-3:
        if sum(alist[0:left]) == sum(alist[right+1:]):
            for item in range(left+2,right-1):
                if sum(alist[left+1:item])==sum(alist[item+1:right])and sum(alist[left+1:item])==sum(alist[0:left]):
                    return True
            right-=1
            left+=1
        elif sum(alist[0:left]) > sum(alist[right+1:]):
            right-=1
        else:
            left+=1
    return False

alist = [2,5,1,1,1,1,4,1,7,3,7]
a2list=[10,2,11,13,1,1,1,1,1]
print(divideList(a2list))