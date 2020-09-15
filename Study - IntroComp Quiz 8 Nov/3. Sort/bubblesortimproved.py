def bubbleSort(alist):
    for passnum in range(len(alist)-1):
        swapped = False
        for i in range(len(alist)-passnum-1):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp
                swapped = True
        print("pass",passnum+1, ":",alist)
        if not swapped:
            break;
        
alist = [3,8,175,20,11]
bubbleSort(alist)
print(alist)
