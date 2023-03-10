def tribonacci(num):
    tribonacci = [1, 0, 0]
    for nums in range(final_num):
        number = sum(tribonacci)
        print(number, end=" ")
        tribonacci.append(number)
        tribonacci.pop(0)


final_num = int(input())
tribonacci(final_num)
