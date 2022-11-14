elements = input().split()
number_of_elements = {}

for element in elements:
    element_lower = element.lower()
    if element_lower not in number_of_elements:
        number_of_elements[element_lower] = 0
    number_of_elements[element_lower] += 1

for key, value in number_of_elements.items():
    if value % 2 != 0:
        print(key, end=" ")
