import datetime
from os import system as os_sys
import random


def lst_state(pl):
    lst_win = list()
    lst_win += [''.join(pl[i][j] for j in range(3)) for i in range(3)]  # Горизонтальные линии
    lst_win += [''.join(pl[j][i] for j in range(3)) for i in range(3)]  # Вертикальные линии
    lst_win.append(''.join(pl[i][-(i-2)] for i in range(3)))  # Диагональ от 13 до 31
    lst_win.append(''.join(pl[i][i] for i in range(3)))  # Диагональ от 11 до 33
    return lst_win


def check_win(pl):
    lst_win = lst_state(pl)
    return 'XXX' in lst_win or 'OOO' in lst_win


def player_hit(pl):
    hit = 0
    while True:
        try:
            hit = int(input('Твой ход (вертикаль-горизонталь): '))
        except ValueError:
            print('Ты ввел что-то не то. Попробуй ещё раз')
            continue
        if hit not in [11, 12, 13, 21, 22, 23, 31, 32, 33]:
            print('Ты ввел что-то не то. Попробуй ещё раз')
            continue
        if pl[(hit // 10)-1][(hit % 10)-1] != ' ':
            print('Эта клетка уже занята, давай другую')
            continue
        else:
            break
    return hit


def computer_hit(pl, c_h, w_s):
    if c_h == 1:
        return 22
    elif c_h == 2 and pl[1][1] == ' ':
        return 22
    elif c_h == 2 and pl[1][1] != ' ':
        return random.choice([11, 13, 31, 33])
    pre_win_combo = ['++ ', '+ +', ' ++']
    l_s = lst_state(pl)
    for j in ['C', 'P']:
        index, combo = -1, -1
        for i in pre_win_combo:
            try:
                index = l_s.index(i.replace('+', w_s[j]))
                combo = i
            except ValueError:
                pass
            if index != -1:
                break
        if combo == '++ ':
            if 0 <= index <= 2:
                return ((index+1) * 10) + 3
            elif 3 <= index <= 5:
                return 28 + index
        elif combo == '+ +':
            if 0 <= index <= 2:
                return ((index+1) * 10) + 2
            elif 3 <= index <= 5:
                return 18 + index
            else:
                return 22

        elif combo == ' ++':
            if 0 <= index <= 2:
                return ((index+1) * 10) + 1
            elif 3 <= index <= 5:
                return 16 - index
    while True:
        y = random.randint(1, 3)
        x = random.randint(1, 3)
        if pl[y-1][x-1] != ' ':
            continue
        else:
            break
    return y*10+x


def draw_place(sc, pl, player, w_s):
    os_sys('cls')
    print(f"Общий счет. {player} {sc['P']} ({w_s['P']}) - 3Ton {sc['C']} ({w_s['C']})")
    print('  1 2 3')
    for i in range(3):
        print(u' \u250C\u2500\u252C\u2500\u252C\u2500\u2510')if i == 0 \
            else print(u' \u251C\u2500\u253C\u2500\u253C\u2500\u2524')
        for i1 in range(3):
            print(i+1, u'\u2502', pl[i][i1], sep='',  end='') if i1 == 0 \
                else print(u'\u2502', pl[i][i1], sep='',  end='')
        else:
            print(u'\u2502')
    else:
        print(u' \u2514\u2500\u2534\u2500\u2534\u2500\u2518')


score = {'P': 0, 'C': 0}
os_sys('cls')
print('Привет! Меня зовут 3Ton, я суперкомпьютер по игре в Крестики Нолики')
player_name = input('Представься пожалуйста. Как тебя зовут?: ')
print(f'Привет {player_name}. Расскажу кратко как будет проходить игра. Общие правила ты, надеюсь, знаешь. \n'
      f'А теперь подробности. Крестики начинают партию. Каждую партию мы меняемся местами. Для того что бы сделать \n'
      f'ход надо ввести номер клетки. Номер клетки это двухзначное число которое определяется как в "морском бое", \n'
      f'первая цифра вертикаль, вторая горизонталь, т.е. левая верхняя клетка это 11, а правая нижняя - это 33. \n'
      f'Извини за такую корявость, графический интерфейс будет в следующей версии когда разработчик изучит Tkinter )))')
print('Ладно. Хватит разговоров. Проведем жеребьевку кто будет первым играть крестиками.')
what_symbols = {'P': 'X', 'C': 'O'} if random.choice(['P', 'C']) == 'P' else {'C': 'X', 'P': 'O'}
print('Я тут подкинул монетку. Первый крестиками играешь Ты') if what_symbols['P'] == 'X' else (
    print('Я тут подкинул монетку. Первый крестиками играю Я. Верь мне на слово )))'))
input('Для продолжения нажмите Enter')
os_sys('cls')
count_match = 0
with open('3Ton.log', 'a+', encoding='utf-8') as log_file:
    print('Партия начата ', datetime.datetime.now(), file=log_file)
while True:
    place = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    who_play = 'P' if what_symbols['P'] == 'X' else 'C'
    count_match += 1
    loggers = dict()
    loggers['Матч'] = count_match
    loggers['Соперник'] = player_name
    count_hit = 0
    while True:
        count_hit += 1
        draw_place(score, place, player_name, what_symbols)
        if who_play == 'P':
            hit_position = player_hit(place)
        else:
            hit_position = computer_hit(place, count_hit, what_symbols)
        place[(hit_position // 10) - 1][(hit_position % 10) - 1] = what_symbols[who_play]
        loggers['Ход ' + str(count_hit)] = [who_play, what_symbols[who_play], str(hit_position)]
        if check_win(place):
            draw_place(score, place, player_name, what_symbols)
            winner = player_name if who_play == 'P' else '3Ton'
            print(f'ПОБЕДА!!! {winner} выиграл этот раунд, ему +1')
            score[who_play] += 1
            what_symbols['P'], what_symbols['C'] = what_symbols['C'], what_symbols['P']
            break
        if ' ' not in place[0] and ' ' not in place[1] and ' ' not in place[2]:
            draw_place(score, place, player_name, what_symbols)
            print('БОЕВАЯ НИЧЬЯ!!! Никому счет не увеличиваем.')
            what_symbols['P'], what_symbols['C'] = what_symbols['C'], what_symbols['P']
            break
        who_play = 'P' if who_play == 'C' else 'C'
    with open('3Ton.log', 'a+', encoding='utf-8') as log_file:
        print(loggers, file=log_file)
    if input('Будем играть еще? (Да(или Enter)/Нет) ') == 'Нет':
        print('Конец игры!')
        break
