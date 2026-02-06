nums = []


def load(list):
    x = range(1000)
    for n in x:
        nums.append(n)


load(nums)

print(len(nums))

start = 0
end = len(nums) - 1
target = 740


def binary_search(num_list, start, end, target):
    if start > end:
        return False
    mid_index = (start + end) // 2
    print(num_list[mid_index])
    if num_list[mid_index] == target:
        return True
    if num_list[mid_index] > target:

        return binary_search(num_list, start, mid_index - 1, target)
    else:
        return binary_search(num_list, mid_index + 1, end, target)


print(binary_search(nums, start, end, target))
