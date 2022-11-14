player_info = input()

all_player_info = {}
total_score_player = []

while player_info != "Season end":

    if '->' in player_info:
        player_info = player_info.split(' -> ')
        p_name = player_info[0]
        p_position = player_info[1]
        p_score = int(player_info[2])
        if p_name not in all_player_info:
            all_player_info[p_name] = all_player_info.get(p_name, {})
            all_player_info[p_name][p_position] = all_player_info[p_name].get(p_position, 0)
            if all_player_info[p_name][p_position] < p_score:
                all_player_info[p_name][p_position] = p_score
            else:
                all_player_info[p_name][p_position] = p_score
        else:
            all_player_info[p_name][p_position] = 0
            if all_player_info[p_name][p_position] < p_score:
                all_player_info[p_name][p_position] = p_score
            else:
                all_player_info[p_name][p_position] = p_score
    elif 'vs' in player_info:
        players_name = player_info.split(' vs ')
        player_one = players_name[0]
        player_two = players_name[1]

        if player_one in all_player_info and player_two in all_player_info:
            for player_1 in all_player_info[player_one]:
                if player_1 in all_player_info[player_two]:
                    total_score_p1 = sum(all_player_info[player_one].values())
                    total_score_p2 = sum(all_player_info[player_two].values())
                    if total_score_p1 > total_score_p2:
                        del all_player_info[player_two]
                    elif total_score_p1 < total_score_p2:
                        del all_player_info[player_one]
                    break


    player_info = input()


for name in all_player_info:
    total_score_player.append({"name": name, "score": sum(all_player_info[name]. values())})
for result in sorted(total_score_player, key=lambda x: (-x['score'], x['name'])):
    print(f"{result['name']}: {result['score']} skill")
    for pos, score in sorted(all_player_info[result['name']].items(), key=lambda x: (-x[1], x[0])):
        print(f"- {pos} <::> {score}")