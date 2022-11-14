string = input()
parantheses = []

for i in range(len(string)):
    if string[i] == "(":
        parantheses.append(i)
    elif string[i] == ")":
        start_index = parantheses.pop()
        print(string[start_index:i + 1])
