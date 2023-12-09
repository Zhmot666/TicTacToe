import os
import random


class TicTacToe:
    player_score = 0
    computer_score = 0
    count_hit = 0
    player_mark = ''
    computer_mark = ''
    player_name = ''
    exit_game = True
    place = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    who_hit = ''

    def __init__(self):
        mark_list = ['X', 'O']
        print('Привет! Меня зовут 3Ton, я суперкомпьютер по игре в Крестики Нолики')
        self.player_name = input('Представься пожалуйста. Как тебя зовут?: ')
        print(f'Привет {self.player_name}. Расскажу кратко как будет проходить игра. Общие правила ты, надеюсь, \n'
              f'знаешь. А теперь подробности. Крестики начинают партию. Каждую партию мы меняемся местами. Для того \n'
              f'что бы сделать ход надо ввести номер клетки. Номер клетки это двухзначное число которое определяется \n'
              f'как в "морском бое", первая цифра вертикаль, вторая горизонталь, т.е. левая верхняя клетка это 11, а \n'
              f'правая нижняя - это 33. Извини за такую корявость, графический интерфейс будет в следующей версии \n'
              f'когда разработчик изучит QT )))')
        print('Ладно. Хватит разговоров. Проведем жеребьевку кто будет первым играть крестиками.')
        self.player_mark = random.choice(mark_list)
        self.computer_mark = 'O' if self.player_mark == 'X' else 'X'
        print('Я тут подкинул монетку. Первый крестиками играешь Ты') if self.player_mark == 'X' else (
            print('Я тут подкинул монетку. Первый крестиками играю Я. Верь мне на слово )))'))
        input('Для продолжения нажмите Enter')

    @staticmethod
    def clear_windows():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def clear_space(self):
        self.place = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def draw_place(self):
        self.clear_windows()
        print(f"Общий счет. {self.player_name} {self.player_score} ({self.player_mark}) - 3Ton {self.computer_score} "
              f"({self.computer_mark})")
        print('  1 2 3')
        for i in range(3):
            print(u' \u250C\u2500\u252C\u2500\u252C\u2500\u2510') if i == 0 \
                else print(u' \u251C\u2500\u253C\u2500\u253C\u2500\u2524')
            for i1 in range(3):
                print(i + 1, u'\u2502', self.place[i][i1], sep='', end='') if i1 == 0 \
                    else print(u'\u2502', self.place[i][i1], sep='', end='')
            else:
                print(u'\u2502')
        else:
            print(u' \u2514\u2500\u2534\u2500\u2534\u2500\u2518')

    def create_list_state(self):
        lst_win = list()
        lst_win += [''.join(self.place[i][j] for j in range(3)) for i in range(3)]  # Горизонтальные линии
        lst_win += [''.join(self.place[j][i] for j in range(3)) for i in range(3)]  # Вертикальные линии
        lst_win.append(''.join(self.place[i][-(i - 2)] for i in range(3)))  # Диагональ от 13 до 31
        lst_win.append(''.join(self.place[i][i] for i in range(3)))  # Диагональ от 11 до 33
        return lst_win

    def control_git(self):  # Откуда оно тут взялось?
        pass

    def hit(self, hit_position, who_hit):
        mark = self.player_mark if who_hit == 'P' else self.computer_mark
        self.place[(hit_position // 10) - 1][(hit_position % 10) - 1] = mark

    def player_hit(self):
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
            if self.place[(hit // 10) - 1][(hit % 10) - 1] != ' ':
                print('Эта клетка уже занята, давай другую')
                continue
            else:
                break
        self.hit(hit, 'P')

    def computer_hit(self):
        if self.count_hit == 1:
            self.hit(22, 'C')
            return
        elif self.count_hit == 2 and self.place[1][1] == ' ':
            self.hit(22, 'C')
            return
        elif self.count_hit == 2 and self.place[1][1] != ' ':
            self.hit(random.choice([11, 13, 31, 33]), 'C')
            return
        pre_win_combo = ['++ ', '+ +', ' ++']
        l_s = self.create_list_state()
        for j in [self.computer_mark, self.player_mark]:
            index, combo = -1, -1
            for i in pre_win_combo:
                try:
                    index = l_s.index(i.replace('+', j))
                    combo = i
                except ValueError:
                    pass
                if index != -1:
                    break
            if combo == '++ ':
                if 0 <= index <= 2:
                    self.hit(((index + 1) * 10) + 3, 'C')
                    return
                elif 3 <= index <= 5:
                    self.hit(28 + index, 'C')
                    return
                elif index == 6:
                    self.hit(31, 'C')
                    return
                elif index == 7:
                    self.hit(33, 'C')
                    return
            elif combo == '+ +':
                if 0 <= index <= 2:
                    self.hit(((index + 1) * 10) + 2, 'C')
                    return
                elif 3 <= index <= 5:
                    self.hit(18 + index, 'C')
                    return
                else:
                    self.hit(22, 'C')
                    return
            elif combo == ' ++':
                if 0 <= index <= 2:
                    self.hit(((index + 1) * 10) + 1, 'C')
                    return
                elif 3 <= index <= 5:
                    self.hit(16 - index, 'C')
                    return
                elif index == 6:
                    self.hit(13, 'C')
                    return
                elif index == 7:
                    self.hit(11, 'C')
                    return
        while True:
            y = random.randint(1, 3)
            x = random.randint(1, 3)
            if self.place[y - 1][x - 1] != ' ':
                continue
            else:
                break
        self.hit(y * 10 + x, 'C')

    def check_win(self):
        lst_win1 = self.create_list_state()
        if 'XXX' in lst_win1 or 'OOO' in lst_win1:
            print('Кто-то победил')
            if self.who_hit == 'P':
                self.player_score += 1
            else:
                self.computer_score += 1
            winner = self.player_name if self.who_hit == 'P' else '3Ton'
            print(f'ПОБЕДА!!! {winner} выиграл этот раунд, ему +1')
            print(f'Текущий счет {self.player_name} {self.player_score} - {self.computer_score} 3Ton ')
            return True
        elif self.count_hit == 9:
            print('БОЕВАЯ НИЧЬЯ!!! Никому счет не увеличиваем.')
            print(f'Текущий счет {self.player_name} {self.player_score} - {self.computer_score} 3Ton ')
            return True

    def question_exit(self):
        answer = input('Будем играть еще? ("Да"(или Enter)/"Нет") ')
        self.exit_game = True if answer == 'Да' or answer == '' else False

    def play(self):
        while self.exit_game:
            self.clear_space()
            self.draw_place()
            self.count_hit = 1
            self.who_hit = 'P' if self.player_mark == 'X' else 'C'
            while True:
                self.player_hit() if self.who_hit == 'P' else self.computer_hit()
                self.draw_place()
                if self.check_win():
                    break
                self.who_hit = 'P' if self.who_hit == 'C' else 'C'
                self.count_hit += 1

            self.player_mark, self.computer_mark = self.computer_mark, self.player_mark
            self.question_exit()


if __name__ == "__main__":
    game = TicTacToe()
    game.play()
