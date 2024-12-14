def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    bubble_sort(arr)
    for x in arr:
        print(x, end=' ')
