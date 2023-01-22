def genrange(start, end):
    num = 0
    while num <= end:
        for i in range(start, end+1):
            yield num + i
        return num


print(list(genrange(1, 10)))





