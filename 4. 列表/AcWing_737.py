nums = []

for i in range(10):
    x = int(input())
    nums.append(x)

for idx in range(10):
    if nums[idx] <= 0:
        nums[idx] = 1
    print("X[%d] = %d" % (idx, nums[idx]))
