class dictionary_iter:

    def __init__(self, dictionary: dict):
        self.key_value = list(dictionary.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.key_value):
            raise StopIteration
        x = self.key_value[self.index]
        self.index += 1
        return x







result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)