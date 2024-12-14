def find_most_frequent(nums):
    count_dict = {}
    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1
    max_frequency = max(count_dict.values())
    most_frequent = [num for num, freq in count_dict.items() if freq == max_frequency]
    return min(most_frequent)

n = int(input())
nums = list(map(int, input().split()))
print(find_most_frequent(nums))
