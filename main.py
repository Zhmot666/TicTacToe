import datetime
import os
import random
import json


def clear_windows():
    """Очищает экран"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def lst_state(pl):
    """Разбивает двумерный массив игрового поля на строки по три символа и складывает в список для дальнейшего анализа

    :param pl:
    :return: lst_win: list() - список состояний строк, столбцов и диагоналей игрового поля
    """
    lst_win = list()
    lst_win += [''.join(pl[i][j] for j in range(3)) for i in range(3)]  # Горизонтальные линии
    lst_win += [''.join(pl[j][i] for j in range(3)) for i in range(3)]  # Вертикальные линии
    lst_win.append(''.join(pl[i][-(i-2)] for i in range(3)))  # Диагональ от 13 до 31
    lst_win.append(''.join(pl[i][i] for i in range(3)))  # Диагональ от 11 до 33
    return lst_win


def check_win(pl):
    """Проверка состояния игрового поля на наличие выигрышной комбинации

    Параметры:
        pl (): Массив игрового поля
    Возвращаемое значение:
        _ bool: Возвращает True если в списке обнаружены последовательности "XXX" или "OOO" обозначающие победу
                иначе False
    """
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


def computer_hit(pl, c_h, w_s, c_c):
    if c_c:
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
                elif index == 6:
                    return 31
                elif index == 7:
                    return 33
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
                elif index == 6:
                    return 13
                elif index == 7:
                    return 11
    while True:
        y = random.randint(1, 3)
        x = random.randint(1, 3)
        if pl[y-1][x-1] != ' ':
            continue
        else:
            break
    return y*10+x


def draw_place(sc, pl, player, w_s):
    """Рисует игровое поле

    :param sc:
    :param pl:
    :param player:
    :param w_s:
    :return:
    """
    clear_windows()
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


if __name__ == "__main__":
    score = {'P': 0, 'C': 0}
    clear_windows()
    print('Привет! Меня зовут 3Ton, я суперкомпьютер по игре в Крестики Нолики')
    player_name = input('Представься пожалуйста. Как тебя зовут?: ')
    print(f'Привет {player_name}. Расскажу кратко как будет проходить игра. Общие правила ты, надеюсь, знаешь. \n'
          f'А теперь подробности. Крестики начинают партию. Каждую партию мы меняемся местами. Для того что бы \n'
          f'сделать ход надо ввести номер клетки. Номер клетки это двухзначное число которое определяется как \n'
          f'в "морском бое", первая цифра вертикаль, вторая горизонталь, т.е. левая верхняя клетка это 11, а \n'
          f'правая нижняя - это 33. Извини за такую корявость, графический интерфейс будет в следующей версии когда \n'
          f'разработчик изучит Tkinter )))')
    print('Ладно. Хватит разговоров. Проведем жеребьевку кто будет первым играть крестиками.')
    what_symbols = {'P': 'X', 'C': 'O'} if random.choice(['P', 'C']) == 'P' else {'C': 'X', 'P': 'O'}
    print('Я тут подкинул монетку. Первый крестиками играешь Ты') if what_symbols['P'] == 'X' else (
        print('Я тут подкинул монетку. Первый крестиками играю Я. Верь мне на слово )))'))
    input('Для продолжения нажмите Enter')
    clear_windows()
    count_party = 0
    loggers = dict()
    loggers['Соперник'] = player_name
    while True:
        place = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        who_play = 'P' if what_symbols['P'] == 'X' else 'C'
        count_party += 1
        loggers['Партия ' + str(count_party)] = dict()
        loggers['Партия ' + str(count_party)]['Кто начал'] = who_play
        hit_list = list()
        count_hit = 0
        while True:
            count_hit += 1
            draw_place(score, place, player_name, what_symbols)
            if who_play == 'P':
                hit_position = player_hit(place)
            else:
                control_computer = True
                hit_position = computer_hit(place, count_hit, what_symbols, control_computer)
                if place[(hit_position // 10) - 1][(hit_position % 10) - 1] != ' ':
                    print('Компьютер допустил ошибку в расчетах. Ход будет сгенерирован в случайную пустую клетку. '
                          'Читайте лог-файл для выяснения обстоятельств.')
                    control_computer = False
                if not control_computer:
                    hit_position = computer_hit(place, count_hit, what_symbols, control_computer)
            hit_list.append(hit_position)
            place[(hit_position // 10) - 1][(hit_position % 10) - 1] = what_symbols[who_play]
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
            loggers['Партия ' + str(count_party)]['Ходы'] = hit_list
        if input('Будем играть еще? (Да(или Enter)/Нет) ') == 'Нет':
            print('Конец игры!')
            break
    if not os.path.exists('Logs'):
        os.mkdir('Logs')
    file_name = 'Logs\\' + str(datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')) + '.json'
    with open(file_name, 'w', encoding='utf-8') as log_file:
        json.dump(loggers, log_file, ensure_ascii=False, indent=4)
