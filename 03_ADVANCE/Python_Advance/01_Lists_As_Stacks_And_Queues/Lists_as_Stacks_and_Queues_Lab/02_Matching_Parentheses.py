# string = input()
# parantheses = []
#
# for i in range(len(string)):
#     if string[i] == "(":
#         parantheses.append(i)
#     elif string[i] == ")":
#         start_index = parantheses.pop()
#         print(string[start_index:i + 1])

class Parentheses:

    def __init__(self, string):
        self.string = string
        self.open_bracket = []
        self.main()

    def main(self):
        for i in range(len(self.string)):
            if self.string[i] == '(':
                self.open_bracket.append(i)
            elif self.string[i] == ')':
                index = self.open_bracket.pop()
                print(self.string[index:i + 1])

bracket = Parentheses(input())