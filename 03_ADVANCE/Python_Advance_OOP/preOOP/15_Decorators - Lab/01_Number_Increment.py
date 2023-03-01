def number_increment(nums):
    def increment():
        return [x + 1 for x in nums]

    return increment()











print(number_increment([1, 2, 3]))
