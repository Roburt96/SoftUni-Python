strings_command = input()
resource_dict = {}
inputs_list = []
while strings_command != "stop":
    inputs_list.append(strings_command)

    if len(inputs_list) == 2:
        if inputs_list[0] not in resource_dict:
            resource_dict[inputs_list[0]] = 0
            resource_dict[inputs_list[0]] += int(inputs_list[-1])
        else:
            resource_dict[inputs_list[0]] += int(inputs_list[-1])
        inputs_list.clear()

    strings_command = input()

for key, value in resource_dict.items():
    print(f"{key} -> {value}")


# resource = {}
#
# while True:
#     command = input()
#
#     if command == 'stop':
#         break
#
#     resours = command
#     quantity = int(input())
#
#     if resours not in resource:
#         resource[resours] = 0
#     resource[resours] += quantity
#
# for key, value in resource.items():
#     print(f"{key} -> {value}")
