def operate(operator, *args):

    def addition(*nums):
        return sum(nums)

    def subtraction(*nums):
        result = 0
        for num in nums:
            result -= num
        return result

    def multiply(*nums):
        result = 1
        for num in nums:
            result *= num
        return result

    def divide(*nums):
        if nums:
            result = nums[0]
            for i in range(1,len(nums)):
                if nums[i] != 0:
                    result /= nums[i]
        return result
    if operator == '+':
        return addition
    elif operator == '-':
        return subtraction
    elif operator == '*':
        return multiply
    elif operator == '/':
        return divide
operation = operate('/')
result = operation(1, 2, 3)
print(result)
# print(operate("+", 1, 2, 3))
# print(operate("*", 3, 4))