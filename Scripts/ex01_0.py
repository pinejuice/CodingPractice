import numpy as np

status = {
    'B': 1,
    'W': -1,
    '': 0,
    'wall': 2
}
length = 8

class OTHELLO():
    def __init__(self):
        # 盤面作成
        self.board = np.zeros((length + 2, length + 2), dtype=int)
        # 壁の作成
        self.board[0, :] = status['wall']
        self.board[:, 0] = status['wall']
        self.board[length + 1, :] = status['wall']
        self.board[:, length + 1] = status['wall']
        # 初期設定
        self.board[4, 4] = status['W']
        self.board[4, 5] = status['B']
        self.board[5, 4] = status['B']
        self.board[5, 5] = status['W']

    def set_stone(self, stone):
        # 指定した場所に石を置く
        self.board[int(stone[1]), int(stone[2])] = stone[0]
        # 挟まれた石をひっくり返す
        self.change_stone(set_info=stone)

    def change_stone(self, set_info):
        # すぐ左に置いた色と異なる色がある場合
        change_stone = []
        if self.board[set_info[1] - 1, set_info[2]] == - set_info[0]:
            change_stone.append([set_info[1] - 1, set_info[2]])
            x = set_info[1] - 2
            y = set_info[2]
            # 置いた色と異なる色がある限り繰り返す
            while self.board[x, y] == - set_info[0]:
                change_stone.append([x, y])
                x -= 1
            # 置いた色と異なる色が無くなった時に置いた色と同じ色があった場合
            if self.board[x, y] == set_info[0]:
                # 挟まれた石をひっくり返す
                for s in change_stone:
                    self.board[s[0], s[1]] = set_info[0]

        # すぐ左上に置いた色と異なる色がある場合
        change_stone = []
        if self.board[set_info[1] - 1, set_info[2] - 1] == - set_info[0]:
            change_stone.append([set_info[1] - 1, set_info[2] - 1])
            x = set_info[1] - 2
            y = set_info[2] - 2
            # 置いた色と異なる色がある限り繰り返す
            while self.board[x, y] == - set_info[0]:
                change_stone.append([x, y])
                x -= 1
                y -= 1
            # 置いた色と異なる色が無くなった時に置いた色と同じ色があった場合
            if self.board[x, y] == set_info[0]:
                # 挟まれた石をひっくり返す
                for s in change_stone:
                    self.board[s[0], s[1]] = set_info[0]

        # すぐ上に置いた色と異なる色がある場合
        change_stone = []
        if self.board[set_info[1], set_info[2] - 1] == - set_info[0]:
            change_stone.append([set_info[1], set_info[2] - 1])
            x = set_info[1]
            y = set_info[2] - 2
            # 置いた色と異なる色がある限り繰り返す
            while self.board[x, y] == - set_info[0]:
                change_stone.append([x, y])
                y -= 1
            # 置いた色と異なる色が無くなった時に置いた色と同じ色があった場合
            if self.board[x, y] == set_info[0]:
                # 挟まれた石をひっくり返す
                for s in change_stone:
                    self.board[s[0], s[1]] = set_info[0]

        # すぐ右上に置いた色と異なる色がある場合
        change_stone = []
        if self.board[set_info[1] + 1, set_info[2] - 1] == - set_info[0]:
            change_stone.append([set_info[1] + 1, set_info[2] - 1])
            x = set_info[1] + 2
            y = set_info[2] - 2
            # 置いた色と異なる色がある限り繰り返す
            while self.board[x, y] == - set_info[0]:
                change_stone.append([x, y])
                x += 1
                y -= 1
            # 置いた色と異なる色が無くなった時に置いた色と同じ色があった場合
            if self.board[x, y] == set_info[0]:
                # 挟まれた石をひっくり返す
                for s in change_stone:
                    self.board[s[0], s[1]] = set_info[0]

        # すぐ右に置いた色と異なる色がある場合
        change_stone = []
        if self.board[set_info[1] + 1, set_info[2]] == - set_info[0]:
            change_stone.append([set_info[1] + 1, set_info[2]])
            x = set_info[1] + 2
            y = set_info[2]
            # 置いた色と異なる色がある限り繰り返す
            while self.board[x, y] == - set_info[0]:
                change_stone.append([x, y])
                x += 1
            # 置いた色と異なる色が無くなった時に置いた色と同じ色があった場合
            if self.board[x, y] == set_info[0]:
                # 挟まれた石をひっくり返す
                for s in change_stone:
                    self.board[s[0], s[1]] = set_info[0]

        # すぐ右下に置いた色と異なる色がある場合
        change_stone = []
        if self.board[set_info[1] + 1, set_info[2] + 1] == - set_info[0]:
            change_stone.append([set_info[1] + 1, set_info[2] + 1])
            x = set_info[1] + 2
            y = set_info[2] + 2
            # 置いた色と異なる色がある限り繰り返す
            while self.board[x, y] == - set_info[0]:
                change_stone.append([x, y])
                x += 1
                y += 1
            # 置いた色と異なる色が無くなった時に置いた色と同じ色があった場合
            if self.board[x, y] == set_info[0]:
                # 挟まれた石をひっくり返す
                for s in change_stone:
                    self.board[s[0], s[1]] = set_info[0]

        # すぐ下に置いた色と異なる色がある場合
        change_stone = []
        if self.board[set_info[1], set_info[2] + 1] == - set_info[0]:
            change_stone.append([set_info[1], set_info[2] + 1])
            x = set_info[1]
            y = set_info[2] + 2
            # 置いた色と異なる色がある限り繰り返す
            while self.board[x, y] == - set_info[0]:
                change_stone.append([x, y])
                y += 1
            # 置いた色と異なる色が無くなった時に置いた色と同じ色があった場合
            if self.board[x, y] == set_info[0]:
                # 挟まれた石をひっくり返す
                for s in change_stone:
                    self.board[s[0], s[1]] = set_info[0]

        # すぐ左下に置いた色と異なる色がある場合
        change_stone = []
        if self.board[set_info[1] - 1, set_info[2] + 1] == - set_info[0]:
            change_stone.append([set_info[1] - 1, set_info[2] + 1])
            x = set_info[1] - 2
            y = set_info[2] + 2
            # 置いた色と異なる色がある限り繰り返す
            while self.board[x, y] == - set_info[0]:
                change_stone.append([x, y])
                x -= 1
                y += 1
            # 置いた色と異なる色が無くなった時に置いた色と同じ色があった場合
            if self.board[x, y] == set_info[0]:
                # 挟まれた石をひっくり返す
                for s in change_stone:
                    self.board[s[0], s[1]] = set_info[0]

    def count_stone(self):
        # 結果出力
        b = np.count_nonzero(self.board == status['B'])
        w = np.count_nonzero(self.board == status['W'])
        print(f'{format(b, "02")}-{format(w, "02")}', end='')
        if b > w:
            print(' The black won!')
        elif w > b:
            print(' The white won!')
        else:
            print(' Draw!')

if __name__ == '__main__':
    othello = OTHELLO()
    max_turn = int(input())
    for i in range(max_turn):
        input_info = input().split(' ')
        set_info = [status[input_info[0]], int(input_info[1]), int(input_info[2])]
        othello.set_stone(set_info)
    othello.count_stone()
