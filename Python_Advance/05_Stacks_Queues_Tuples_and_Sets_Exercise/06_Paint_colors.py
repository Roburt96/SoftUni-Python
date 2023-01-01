from collections import deque
colors = deque(input().split())

complete_colors = []

all_colors = {
    'colors': ('red', 'blue', 'yellow', 'orange', 'purple', 'green')
}
secondary_colors = {
    'orange': ('red', 'yellow'),
    'purple': ('red', 'blue'),
    'green': ('yellow', 'blue')
}

while colors:

        second = ''
        if len(colors) > 1:
            second = colors.pop()
        first = colors.popleft()
        for check in (first + second, second + first):
            if check in all_colors['colors']:
                complete_colors.append(check)
                break
        else:
            for item in (first[:-1], second[:-1]):
                if item:
                    colors.insert(len(colors) // 2, item)

for color, req_colors in secondary_colors.items():
    if any(x not in complete_colors and color in complete_colors for x in req_colors):
        complete_colors.remove(color)



print(complete_colors)

