nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    return nums ** 2


def remove_negatives(nums):
    return nums > 0


def choose_func(nums, square, negative):
    if nums == list(filter(lambda x: x > 0, nums)):
        return list(map(square, nums))
    else:
        return list(filter(negative, nums))


print(choose_func(nums1, square_nums, remove_negatives))
print(choose_func(nums2, square_nums, remove_negatives))
