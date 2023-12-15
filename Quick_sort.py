def partition(arr,start,end):
    i = start-1
    pivot = arr[end]
    for j in range(start,end):
        if(arr[j]<=pivot):
            i+1
            arr[i],arr[j]=arr[j],arr[i]
        arr[i+1],arr[end]=arr[end],arr[i+1]
    return i+1
            


def quick_sort(arr,start,end):
    if (start<end):
        p = partition(arr,start,end)
        quick_sort(arr,start,p-1)
        quick_sort(arr,p+1,end)
        

arr = [4,1,7,4,21,44,32,11]

start = 0
end = len(arr)-1
quick_sort(arr,start,end)
print(arr)