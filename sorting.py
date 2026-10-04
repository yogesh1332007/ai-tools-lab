def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


<<<<<<< HEAD
numbers = [64, 34, 25, 12, 24, 11, 90]
=======
numbers = [64, 34,5, 12, 22, 12, 90]
>>>>>>> 14af60654139456c157433ac565cc4b710bb1dcf

print("Original list:", numbers)
print("Sorted list:", bubble_sort(numbers))
