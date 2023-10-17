list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

players_count = len(list_players)
# Первая команда игроков
print(list_players[:players_count // 2])
# Вторая команда игроков
print(list_players[players_count // 2:])
