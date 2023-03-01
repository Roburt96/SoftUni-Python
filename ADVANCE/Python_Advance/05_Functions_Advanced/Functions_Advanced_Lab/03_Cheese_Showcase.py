
def sorting_cheeses(**kwargs):
    sorted_cheeses = {}
    result = ""
    for key, value in sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0])):
        sorted_cheeses[key] = sorted_cheeses.get(key, []) + [str(x) for x in sorted(value, reverse=True)]
    for name in sorted_cheeses:
        result += f"{name}\n"
        for price in sorted_cheeses[name]:
            result += f"{price}\n"
    return result


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)