regular_guest = set()
vip_guest = set()
total_guest = set()
number_of_guests = int(input())

for i in range(number_of_guests):
    guest_ticket = input()
    total_guest.add(guest_ticket)
    for ch in guest_ticket:
        if ch.isdigit():
            vip_guest.add(guest_ticket)
            break
        elif ch.isalpha():
            regular_guest.add(guest_ticket)
            break

guest_who_come_to_party = input()
while guest_who_come_to_party != 'END':
    if guest_who_come_to_party in regular_guest:
        regular_guest.discard(guest_who_come_to_party)
        total_guest.discard(guest_who_come_to_party)
    elif guest_who_come_to_party in vip_guest:
        vip_guest.discard(guest_who_come_to_party)
        total_guest.discard(guest_who_come_to_party)

    guest_who_come_to_party = input()

print(len(total_guest))
for not_come in sorted(total_guest):
    print(not_come)
