companies_info = {}

command = input()

while command != 'End':
    company_name, employee_id = [x for x in command.split(" -> ")]

    if company_name not in companies_info:
        companies_info[company_name] = [employee_id]
    else:
        if employee_id not in companies_info[company_name]:
            companies_info[company_name].append(str(employee_id))
            # for key, value in companies_info.items():
            #     companies_info[key] = list(value)

    command = input()

for k, v in companies_info.items():
    print(f"{k}")
    for v in companies_info[k]:
        print(f"-- {''.join(v)}")
