from collections import deque
presents = {
    "Doll": 0,
    "Wooden train": 0,
    "Teddy bear": 0,
    "Bicucle": 0
}
needed = {
    150: "Doll",
    250: "Wooden train",
    350: "Teddy bear",
    400: "Bicycle"
}

materials = deque(int(x) for x in input())   # pop
magic = deque(int(x) for x in input())       # popleft



