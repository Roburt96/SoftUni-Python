data_type = input()
data = input()


def calc(data1, data2):
    result = ""
    if data1 == "int":
        result = int(data2) * 2
       # return f"{result:.0f}"

    elif data1 == "real":
        result = f"{float(data2) * 1.5:.2f}"
       # return f"{result:.2f}"

    elif data1 == "string":
        result = f"${data2}$"
       #  return f"${data2}$"

    return result


print(calc(data_type, data))
