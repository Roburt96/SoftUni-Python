import re

pattern = re.compile(r'(@)(#+)(?P<word>[A-Z][a-zA-Z0-9]{4,}[A-Z])(@)(#+)')

num_of_barcode = int(input())

for i in range(num_of_barcode):
    barcode = input()

    result = list(re.finditer(pattern, barcode))
    pattern_digits = re.compile(r'[0-9]+')
    result_digits = re.finditer(pattern_digits, barcode)
    list_result_digits = [x[0] for x in result_digits]

    if len(list_result_digits) == 0:
        if result:
            print(f"Product group: 00")
        else:
            print('Invalid barcode')
    elif len(list_result_digits) > 0:
        print(f"Product group: {''.join(list_result_digits)}")
