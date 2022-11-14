number_of_inputs = int(input())

start_name = 0
start_age = 0
end_name = 0
end_age = 0

for i in range(number_of_inputs):
    text = input()
    for z in range(len(text)):
        if text[z] == '@':
            start_name = int(z + 1)
        elif text[z] == '|':
            end_name = int(z)
        if text[z] == '#':
            start_age = int(z + 1)
        elif text[z] == '*':
            end_age = int(z)

    name = text[start_name:end_name]
    age = text[start_age:end_age]
    print(f"{name} is {age} years old.")

# def extracting(input_data):
#     name_start = 0
#     name_end = 0
#     age_start = 0
#     age_end = 0
#     for i in range(len(input_data)):
#         if input_data[i] == "@":
#             name_start = int(i + 1)
#         elif input_data[i] == '|':
#             name_end = int(i)
#         if input_data[i] == '#':
#             age_start = int(i + 1)
#         elif input_data[i] == '*':
#             age_end = int(i)
#     name = input_data[name_start:name_end]
#     age = input_data[age_start:age_end]
#     return f"{name} is {age} years old."
#
# number_line = int(input())
#
# for i in range(number_line):
#     current_data = input()
#     print(extracting(current_data))

