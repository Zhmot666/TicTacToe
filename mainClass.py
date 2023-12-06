import os
import random


class TicTacToe:
    player_score = 0
    computer_score = 0
    player_mark = ''
    computer_mark = ''
    player_name = ''
    exit_game = True
    place = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    who_hit = ''

    def __init__(self):
        mark_list = ['X', 'O']
        self.player_mark = random.choice(mark_list)
        self.computer_mark = 'O' if self.player_mark == 'X' else 'X'
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
        self.who_hit = 'P' if self.player_mark == 'X' else 'C'
        print('Я тут подкинул монетку. Первый крестиками играешь Ты') if self.player_mark == 'X' else (
            print('Я тут подкинул монетку. Первый крестиками играю Я. Верь мне на слово )))'))
        input('Для продолжения нажмите Enter')

    @staticmethod
    def clear_windows():
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def player_win(self):
        print('Игрок победил!')
        self.player_score += 1

    def computer_win(self):
        print('Компьютер победил!')
        self.computer_score += 1

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

    def control_git(self):
        pass

    def player_hit(self):
        pass

    def computer_hit(self):
        pass

    def check_win(self):
        return

    def question_exit(self):
        answer = input('Будем играть еще? (Да(или Enter)/Нет) ')
        self.exit_game = True if answer == 'Да' or answer == '' else False

    def play(self):
        while self.exit_game:
            self.clear_windows()
            self.clear_space()
            while True:
                self.clear_windows()
                self.draw_place()
                self.player_hit() if self.who_hit == 'P' else self.computer_hit()
                self.check_win()
            self.question_exit()



game = TicTacToe()
game.play()
