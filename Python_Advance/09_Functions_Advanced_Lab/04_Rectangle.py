def rectangle(length, width):
    def rectangle_area():
        return length * width

    def rectangle_perimeter():
        return 2 * length + 2 * width

    if isinstance(length, int) or isinstance(width, int):
        return f"Rectangle area: {rectangle_area()}\nRectangle perimeter: {rectangle_perimeter()}"

    else:
        return "Enter valid values!"

print(rectangle(2, 10))