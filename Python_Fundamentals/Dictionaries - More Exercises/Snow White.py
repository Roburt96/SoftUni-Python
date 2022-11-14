
def add_dwarf_(name, color, physics):
    if color not in dwarfs_data:
        dwarfs_data[color] = {}
    if name not in dwarfs_data[color]:
        dwarfs_data[color][name] = 0
    if dwarfs_data[color][name] < physics:
        dwarfs_data[color][name] = physics


dwarfs = input()

dwarfs_data = {}
result_dwarfs = []
name_d = "name"
hat_d = "hat"
physic_d = "physic"
hat_len = "hat len"

while dwarfs != 'Once upon a time':
    dwarfs = dwarfs.split(" <:> ")
    dwarf_name = dwarfs[0]
    dwarf_color = dwarfs[1]
    dwarf_physics = int(dwarfs[2])
    add_dwarf_(dwarf_name, dwarf_color, dwarf_physics)

    dwarfs = input()

for color_hat in dwarfs_data:
    for name, physics in dwarfs_data[color_hat].items():
        result_dwarfs.append({hat_len: len(dwarfs_data[color_hat]), name_d: name, physic_d: physics, hat_d: color_hat})
for result in sorted(result_dwarfs, key=lambda x: (-x[physic_d], -x[hat_len])):
    print(f"({result[hat_d]}) {result[name_d]} <-> {result[physic_d]}")