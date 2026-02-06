def find_duplicate(nums):
    tortoise = nums[0]
    hare = nums[0]

    while True:
        tortoise = nums[tortoise]
        hare = nums[nums[hare]]
        if tortoise == hare:
            break

    tortoise = nums[0]

    while tortoise != hare:
        tortoise = nums[tortoise]
        hare = nums[hare]

    return hare


[3, 4, 4, 4, 2]
[1, 1]
[1, 3, 4, 2, 2]
nums = [1, 3, 6, 2, 7, 3, 5, 4]
[1, 2, 2]
find_duplicate(nums)
