def grocery_store(**kwargs):
    result_order = [f'{key}: {value}' for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], -len([x]), x[1]))]
    return '\n'.join(result_order)









print(grocery_store(bread=5, pasta=12, eggs=12,))

print(grocery_store(bread=2, pasta=2, eggs=20, carrot=1,))