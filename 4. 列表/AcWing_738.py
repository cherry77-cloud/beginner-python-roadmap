n = int(input())

nums = []

for i in range(10):
    nums.append(n)
    n *= 2

for j in range(10):
    print("N[%d] = %d" %(j, nums[j]))
