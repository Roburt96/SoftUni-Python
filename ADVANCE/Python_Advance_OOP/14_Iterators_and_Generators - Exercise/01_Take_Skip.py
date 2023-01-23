class take_skip:

    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.nums = 0
    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        x = self.nums
        self.nums += self.step
        self.count -= 1
        return x





numbers = take_skip(2, 6)
for number in numbers:
    print(number)