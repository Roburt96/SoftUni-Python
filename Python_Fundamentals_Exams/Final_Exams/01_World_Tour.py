travel_stops = input()

command = input()
while command != 'Travel':
    cmd_type, *data = command.split(":")

    if 'Add Stop' in cmd_type:
        index = int(data[0])
        string = data[1]
        if 0 <= index < len(travel_stops):
            travel_stops = travel_stops[:index] + string + travel_stops[index:]
        print(travel_stops)

    elif 'Remove Stop' in cmd_type:
        start_index = int(data[0])
        end_index = int(data[1])
        if 0 <= start_index < len(travel_stops) and 0 <= end_index < len(travel_stops):
            travel_stops = travel_stops[:start_index] + travel_stops[end_index+1:]
        print(travel_stops)

    elif 'Switch' in cmd_type:
        old_string = data[0]
        new_string = data[1]
        if old_string in travel_stops:
            travel_stops = travel_stops.replace(old_string, new_string)
            print(travel_stops)
    command = input()

print(f"Ready for world tour! Planned stops: {travel_stops}")








