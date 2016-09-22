def quick_sort(arr, left, right):
    if left < right:
        base = arr[left]
        a, b = left, right
        while a < b:
            while arr[b] >= base and a < b:
                b -= 1
            while arr[a] <= base and a < b:
                a += 1
            if a < b:
                arr[a], arr[b] = arr[b], arr[a]
        arr[left] = arr[a]
        arr[a] = base
        print arr
        quick_sort(arr, left, a-1)
        quick_sort(arr, a+1, right)
    else:
        return

l = [2,1,3,12,1,2,5,5,6]
quick_sort(l, 0, len(l)-1)
print l
