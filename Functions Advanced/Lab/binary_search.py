def binary_search(nums, searched_num):
    low = 0
    high = len(nums) - 1
    while low <=high:
        middle_index = (low+high)//2
        middle_el = nums[middle_index]
        if middle_el == searched_num:
            return middle_index, middle_el
        if searched_num > middle_el:
            low = middle_index + 1
        else:
            high = middle_index - 1
print(binary_search([1, 34, 56, 87, 199, 233, 600, 1090, 2500, 10000, 10001, 20000], 56))

