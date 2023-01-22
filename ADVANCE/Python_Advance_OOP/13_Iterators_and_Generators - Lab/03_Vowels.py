class vowels:
    all_vowels = ["a", "e", "i", "u", "y", "o"]

    def __init__(self, string):
        self.string = string
        self.vowels = [x for x in self.string if x.lower() in vowels.all_vowels]
        self.start = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start == len(self.vowels):
            raise StopIteration
        x = self.start
        self.start += 1
        return self.vowels[x]

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)