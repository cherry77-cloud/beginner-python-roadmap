def reverse_array(arr):
    start = 0
    end = len(arr) - 1
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr

nums = []

for i in range(20):
    x = int(input())
    nums.append(x)

nums = reverse_array(nums)

for j in range(20):
    print("N[%d] = %d" % (j, nums[j]))
