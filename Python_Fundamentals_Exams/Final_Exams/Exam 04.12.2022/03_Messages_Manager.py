def add_(username, sent, received):
    msg[username] = msg.get(username, {'sent': sent, 'received': received})


def message_(sender, receiver):
    if sender in msg and receiver in msg:
        msg[sender]['sent'] += 1
        msg[receiver]['received'] += 1
        if msg[sender]['sent'] + msg[sender]['received'] >= 10:
            print(f"{sender} reached the capacity!")
            del msg[sender]
        if msg[receiver]['received'] + msg[receiver]['sent'] >= 10:
            print(f"{receiver} reached the capacity!")
            del msg[receiver]


def empty_(username):
    if username in msg:
        del msg[username]


msg = {}
capacity = int(input())
commands = input()
while commands != 'Statistics':
    cmd_type, *data = commands.split("=")
    if 'Add' in cmd_type:
        username, sent, received = data[0], int(data[1]), int(data[2])
        add_(username, sent, received)

    elif 'Message' in cmd_type:
        sender, receiver = data[0], data[1]
        message_(sender, receiver)

    elif 'Empty':
        username = data[0]
        if username == 'All':
            msg = {}
        else:
            empty_(username)

    commands = input()

print(f"Users count: {len(msg)}")
for user, messages in msg.items():
    print(f"{user} - {messages['sent'] + messages['received']}")


