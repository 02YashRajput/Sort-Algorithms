def merge(arr,start,end):
    temp = []
    mid = (start+end)//2
    i = start
    j = mid+1

    while(i<=mid and j <=end):
        if arr[i]<arr[j]:
            temp.append(arr[i])
            i+=1
        else :
            temp.append(arr[j])
            j+=1
    while(i<=mid):
        temp.append(arr[i])
        i+=1
    while(j<=end):
        temp.append(arr[j])
        j+=1
    m =0
    for i in range(0,len(temp)):
        arr[start+m] = temp[m]
        m+=1


def merge_sort(arr,start,end):
    if end<=start:
        return
    mid = (start+end)//2
    merge_sort(arr,start,mid)
    merge_sort(arr,mid+1,end)
    merge(arr,start,end)

arr = [3,1,8,5,12,2]
start = 0
end = len(arr)-1
merge_sort(arr,start,end)
print(arr)


