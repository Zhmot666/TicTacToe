import sys
from PyQt6 import QtWidgets
import design
import random


class TicTacToe:
    player_score = 0
    computer_score = 0
    count_hit = 0
    player_mark = ''
    computer_mark = ''
    player_name = ''
    place = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    who_hit = ''

    def __init__(self, window):
        mark_list = ['X', 'O']
        self.player_name = 'Тест'
        self.player_mark = random.choice(mark_list)
        self.computer_mark = 'O' if self.player_mark == 'X' else 'X'
        window.PlayerName.setText(_translate("Frame", self.player_name))

    def clear_space(self):
        self.place = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

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
            if self.who_hit == 'P':
                self.player_score += 1
            else:
                self.computer_score += 1
            return True
        elif self.count_hit == 9:
            return True


class ExampleApp(QtWidgets.QMainWindow, design.Ui_Frame):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        game = TicTacToe(self)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    # game = TicTacToe(window)
    app.exec()

    # game = TicTacToe()
    # game.play()
    # window.show()


if __name__ == '__main__':
    main()
