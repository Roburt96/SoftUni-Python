# numbers = [int(x) for x in input().split()]
# positive = []
# negative = []
#
# for i in numbers:
#     if i > 0:
#         positive.append(i)
#     elif i < 0:
#         negative.append(i)
#
# print(sum(negative))
# print(sum(positive))
#
# if sum(positive) > abs(sum(negative)):
#     print('The positives are stronger than the negatives')
# else:
#     print('The negatives are stronger than the positives')


def append_(nums, positive, negative):

    for i in nums:
        if i > 0:
            positive.append(i)
        elif i < 0:
            negative.append(i)
    print(sum(negative))
    print(sum(positive))


def main():
    numbers = [int(x) for x in input().split()]
    positive = []
    negative = []
    append_(numbers, positive, negative)
    if sum(positive) > abs(sum(negative)):
        print('The positives are stronger than the negatives')
    else:
        print('The negatives are stronger than the positives')

main()