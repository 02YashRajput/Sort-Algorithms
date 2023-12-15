def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min = i
        for  j in range(i+1,n):
            if arr[min]>arr[j]:
                min = j
        arr[min],arr[i]= arr[i],arr[min]

arr = [1,7,16,9,8,5,2,1]
selection_sort(arr)
print(arr)