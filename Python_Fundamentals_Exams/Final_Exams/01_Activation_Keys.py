activation_key = input()
command = input()

while command != 'Generate':
    cmd_type, *data = command.split(">>>")

    if 'Contains' in cmd_type:
        substring = data[0]
        if substring in activation_key:
            print(f"{activation_key} contains {substring}")
        else:
            print("Substring not found!")

    elif 'Flip' in cmd_type:
        cmd = data[0]
        start_flip_index = int(data[1])
        end_flip_index = int(data[2])
        if 'Upper' in cmd:
            activation_key = activation_key[:start_flip_index] + \
                             (activation_key[start_flip_index:end_flip_index]).upper() + \
                             activation_key[end_flip_index:]
            print(activation_key)

        elif 'Lower' in cmd:
            activation_key = activation_key[:start_flip_index] + \
                             (activation_key[start_flip_index:end_flip_index]).lower() + \
                             activation_key[end_flip_index:]
            print(activation_key)

    elif 'Slice' in cmd_type:
        start_slice_index = int(data[0])
        end_slice_index = int(data[1])
        activation_key = activation_key[:start_slice_index] + activation_key[end_slice_index:]
        print(activation_key)

    command = input()

print(f"Your activation key is: {activation_key}")