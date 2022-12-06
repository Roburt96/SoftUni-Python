def add_(username, sent, received):
    msg[username] = msg.get(username, {'sent': sent, 'received': received})


def message_(sender, receiver):
    if sender in msg and receiver in msg:
        msg[sender]['sent'] += 1
        msg[receiver]['received'] += 1
        if msg[sender]['sent'] >= 10:
            print(f"{sender} reached the capacity!")
            del msg[sender]
        if msg[receiver]['received'] >= 10:
            print(f"{receiver} reached the capacity!")
            del msg[receiver]

msg = {}
capacity = int(input())
commands = input()
while commands != 'Statistics':
    cmd_type, *data = commands.split("=")
    if 'Add' in cmd_type:
        username = data[0]
        sent = int(data[1])
        received = data[2]
        add_(username, sent, received)

    elif 'Message' in cmd_type:
        sender = data[0]
        receiver = data[1]
        message_(sender, receiver)



    commands = input()
