from collections import deque

class Flowers:

    def __init__(self):
        self.vowels = deque(input().split())
        self.consonants = deque(input().split())
        self.flowers = {
            "rose": "rose",
            "tulip": "tulip",
            "lotus": "lotus",
            "daffodil": "daffodil"
        }
        self.find = False
        self.word = ""
        self.main()

    def main(self):
        while self.vowels and self.consonants and not self.find:
            first_character = self.vowels.popleft()
            second_character = self.consonants.pop()
            for key, value in self.flowers.items():
                if first_character in value:
                    self.flowers[key] = self.flowers[key].replace(first_character, "")
                if second_character in value:
                    self.flowers[key] = self.flowers[key].replace(second_character, "")
                if not self.flowers[key]:
                    self.word = key
                    self.find = True
                    break
        if self.find:
            print(f"Word found: {self.word}")
        elif not self.find:
            print("Cannot find any word!")
        if self.vowels:
            print(f"Vowels left: {' '.join(self.vowels)}")
        if self.consonants:
            print(f"Consonants left: {' '.join(self.consonants)}")

if __name__ == '__main__':
    Flowers()
# vowels = deque(input().split())
# consonants = deque(input().split())
# flowers = {
#     "rose": "rose",
#     "tulip": "tulip",
#     "lotus": "lotus",
#     "daffodil": "daffodil"
# }
#
# find = False
# word = ""
#
# while vowels and consonants and not find:
#     first_ch = vowels.popleft()
#     second_ch = consonants.pop()
#     for key, value in flowers.items():
#         if first_ch in value:
#             flowers[key] = flowers[key].replace(first_ch, "")
#         if second_ch in value:
#             flowers[key] = flowers[key].replace(second_ch, "")
#         if not flowers[key]:
#             word = key
#             find = True
#             break
#
# if find:
#     print(f"Word found: {word}")
# elif not find:
#     print("Cannot find any word!")
# if vowels:
#     print(f"Vowels left: {' '.join(vowels)}")
# if consonants:
#     print(f"Consonants left: {' '.join(consonants)}")
