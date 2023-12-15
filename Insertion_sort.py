def inserion_sort(arr):
    n = len(arr)
    for j in range(1,len(arr)):
        key = arr[j]
        i = j-1
        while(i>=0 and key<arr[i]):
            arr[i+1] = arr[i]
            i-=1
        arr[i+1] = key

arr = [1,7,16,9,8,5,2,1]
inserion_sort(arr)
print(arr)