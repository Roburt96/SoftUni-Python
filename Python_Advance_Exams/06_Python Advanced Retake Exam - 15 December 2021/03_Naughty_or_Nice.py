def naughty_or_nice_list(*args, **kwargs):
    santa_dict ={
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }
    santa_list = []

    for num, kid in args:
        num = args[0]
        kid = args[1]

    santa_list = sorted(santa_list)

print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))