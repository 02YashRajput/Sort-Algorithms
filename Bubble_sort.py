def bubble_sort(arr):
    n = len(arr)-1
    for i in range(n):
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],arr[j]


def modified_Bubble_sort(arr):
    n = len(arr)-1
    for i in range(n):
        flag = False
        for j in range(n-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] =arr[j+1],arr[j]
                flag = True
        if flag == False:
            break


arr = [1,7,16,9,8,5,2]
modified_Bubble_sort(arr)
print(arr)