class take_skip:

    def __init__(self, *args):
        self.step = int(args[0])
        self.count = int(args[1])
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        x = self.counter
        self.counter += self.step
        self.count -= 1
        return x



numbers = take_skip(2, 6)
for number in numbers:
    print(number)