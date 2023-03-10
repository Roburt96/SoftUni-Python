followers = {}


def new_follower_(username):
    followers[username] = followers.get(username, {'likes': 0, 'comments': 0})


def like_(username, count):
    if username not in followers:
        followers[username] = followers.get(username, {'likes': count, 'comments': 0})
    else:
        followers[username]['likes'] += count


def comment_(username):
    if username not in followers:
        followers[username] = followers.get(username, {'likes': 0, 'comments': 1})
    else:
        followers[username]['comments'] += 1


def blocked_(username):
    if username in followers:
        del followers[username]
    else:
        print(f"{username} doesn't exist.")


command = input()
while command != 'Log out':
    cmd_type, *data = command.split(": ")
    if cmd_type == 'New follower':
        username = data[0]
        new_follower_(username)

    elif cmd_type == 'Like':
        username = data[0]
        count = int(data[1])
        like_(username, count)

    elif cmd_type == 'Comment':
        username = data[0]
        comment_(username)

    elif cmd_type == 'Blocked':
        username = data[0]
        blocked_(username)

    command = input()

print(f"{len(followers)} followers")
for key, value in followers.items():
    print(f"{key}: {followers[key]['likes'] + followers[key]['comments']}")


