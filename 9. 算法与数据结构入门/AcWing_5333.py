def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap elements
            j -= 1
    return arr


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    insertion_sort(arr)

    for x in arr:
        print(x, end=' ')
