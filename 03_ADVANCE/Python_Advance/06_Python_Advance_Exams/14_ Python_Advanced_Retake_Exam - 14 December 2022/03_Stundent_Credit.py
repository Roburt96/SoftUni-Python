def students_credits(*args):
    credits = {}

    for i in args:
        course, credit, total_point, current_point = i.split("-")
        total_credits = (int(current_point) / int(total_point) * int(credit))
        credits[course] = credits.get(course, total_credits)

    output = ''
    if sum(credits.values()) >= 240:
        output += f"Diyan gets a diploma with {sum(credits.values()):.1f} credits.\n"
    else:
        output += f"Diyan needs {240 - sum(credits.values()):.1f} credits more for a diploma.\n"

    for key, value in sorted(credits.items(), key=lambda x: -x[1]):
        output += f"{key} - {value:.1f}\n"
    return output







# print(
#     students_credits(
#         "Computer Science-12-300-250",
#         "Basic Algebra-15-400-200",
#         "Algorithms-25-500-490"
#     )
# )
print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)