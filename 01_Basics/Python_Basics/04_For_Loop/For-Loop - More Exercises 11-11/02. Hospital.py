period = int(input())
doctors = 7
total_examined_patient = 0
total_unexamined_patient = 0

for review in range(1, period + 1):
    daily_examined_patient = 0
    daily_unexamined_patient = 0

    if review % 3 == 0 and total_unexamined_patient > total_examined_patient:
        doctors += 1
    patients_count = int(input())

    if doctors >= patients_count:
        daily_examined_patient = patients_count
        daily_unexamined_patient = 0

    if doctors < patients_count:
        daily_unexamined_patient = patients_count - doctors
        daily_examined_patient = patients_count - daily_unexamined_patient

    total_unexamined_patient += daily_unexamined_patient
    total_examined_patient += daily_examined_patient

print(f'Treated patients: {total_examined_patient}.')
print(f'Untreated patients: {total_unexamined_patient}.')
