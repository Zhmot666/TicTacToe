import json
import os
from main import draw_place
from main import clear_windows

clear_windows()
if os.path.exists('Logs'):
    files_list = os.listdir('Logs')
    count = 1
    for i in files_list:
        match_time = i.replace('_', ' ').replace('.json', '')
        with open('Logs\\'+i, 'r', encoding='utf-8') as json_file:
            json_data = json.load(json_file)
            player_name = json_data['Соперник']
        print(f'Матч №{count} против {player_name} состоялся {match_time}')
        count += 1
    match_num = int(input('Введите номер матча: '))
    clear_windows()
    print('Список партий:')
    with open('Logs\\' + files_list[match_num-1], 'r', encoding='utf-8') as json_file:
        json_data = json.load(json_file)
        for i in json_data:
            if str(i).find('Партия') != -1:
                print(i, 'Начал', json_data[i]['Кто начал'], 'Ходы: ', end='')
                for value in json_data[i]['Ходы']:
                    print(value, end=' ')
                print()
    party_num = int(input('Введите номер партии для просмотра: '))
    for i in json_data:
        player_name = json_data['Соперник']
        if str(i).find('Партия ' + str(party_num)) != -1:
            who_starter = json_data[i]['Кто начал']
            hit_list = json_data[i]['Ходы']
    score = {'P': '---', 'C': '---'}
    place = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    what_symbols = {'P': 'X', 'C': 'O'} if who_starter == 'P' else {'C': 'X', 'P': 'O'}
    clear_windows()
    draw_place(score, place, player_name, what_symbols)
    print(f'Начинает {player_name}') if who_starter == 'P' else print('Начинает 3Ton')
    input('Для продолжения нажмите Enter')
    count_hit = 1
    for i in hit_list:
        place[(i // 10) - 1][(i % 10) - 1] = 'O' if count_hit % 2 == 0 else 'X'
        count_hit += 1
        draw_place(score, place, player_name, what_symbols)
        input('Для продолжения нажмите Enter')
        clear_windows()
else:
    print('Папка с записями игр не найдена. Воспроизводить нечего :(')
