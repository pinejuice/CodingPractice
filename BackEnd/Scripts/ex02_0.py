import random

player_info = {
    1: 'User',
    -1: 'NPC'
}

class Numeron():
    def __init__(self):
        self.game_digit = 3
        self.set_npc_candidate_list()
        self.npc_set_num = random.choice(self.numbers)
        self.user_set_num = input(f'数字 {self.game_digit} 桁を重複なしで決めてください。')
        self.winner = ''
        self.now_player = 1
        self.npc_not_use_num = []
        self.user_history = []
        self.npc_history = []
    
    def set_npc_candidate_list(self):
        self.numbers = []
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for i in range(0, 10):
            for j in range(0, 10):
                if i == j:
                    continue
                for k in range(0, 10):
                    if j == k or i == k:
                        continue
                    self.numbers.append(nums[i] + nums[j] + nums[k])

    def input_num(self):
        print(f'{player_info[self.now_player]}のターンです。')
        if self.now_player == 1:
            input_number = input(f'{self.game_digit} 桁の相手の数字を入力して下さい。：\n')
        else:
            input_number = random.choice(self.numbers)
            print(input_number)
        eat, bite = self.check_numbers(input_number)
        self.input_history(input_number, eat, bite)
        print(f'{eat} eat, {bite} bite')
        if eat == self.game_digit:
            self.winner = player_info[self.now_player]
            print(f'{self.winner}の勝ちです！')
        else:
            if self.now_player == -1:
                self.check_result(eat, bite, input_number)
                self.history_check()
                print(f'NPCは、{len(self.numbers)}パターンまで絞っています。')

    def check_numbers(self, input_number):
        eat = 0
        bite = 0
        if self.now_player == 1:
            i = 0
            while i < self.game_digit:
                if list(input_number)[i] == list(self.npc_set_num)[i]:
                    eat += 1
                elif list(input_number)[i] in self.npc_set_num:
                    bite += 1
                i += 1
        elif self.now_player == -1:
            i = 0
            while i < self.game_digit:
                if list(input_number)[i] == list(self.user_set_num)[i]:
                    eat += 1
                elif list(input_number)[i] in self.user_set_num:
                    bite += 1
                i += 1
        return eat, bite

    def check_result(self, eat, bite, input_number):
        # npcの選択肢を絞っていく処理
        nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        # 使われていない数字が確定した場合
        if eat == 0 and bite == 0:
            # 未使用の数字を使っている数列を削除
            new_numbers = [n for n in self.numbers if input_number[0] not in n and input_number[1] not in n and input_number[2] not in n]
            self.numbers = new_numbers
            for i in list(input_number):
                self.npc_not_use_num.append(i)

        elif eat == 1 and bite == 0:
            new_numbers = []
            num_list = list(input_number)
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                for j in range(0, len(nums)):
                    if i == j:
                        continue
                    if nums[j] in num_list or nums[j] in self.npc_not_use_num:
                        continue
                    new_numbers.append(num_list[0] + nums[i] + nums[j])
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                for j in range(0, len(nums)):
                    if i == j:
                        continue
                    if nums[j] in num_list or nums[j] in self.npc_not_use_num:
                        continue
                    new_numbers.append(nums[i] + num_list[1] + nums[j])
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                for j in range(0, len(nums)):
                    if i == j:
                        continue
                    if nums[j] in num_list or nums[j] in self.npc_not_use_num:
                        continue
                    new_numbers.append(nums[i] + nums[j] + num_list[2])
            if len(self.numbers) >= len(new_numbers):
                self.numbers = new_numbers

        elif eat == 2 and bite == 0:
            new_numbers = []
            num_list = list(input_number)
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                new_numbers.append(num_list[0] + num_list[1] + nums[i])
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                new_numbers.append(num_list[0] + nums[i] + num_list[2])
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                new_numbers.append(nums[i] + num_list[1] + num_list[2])
            if len(self.numbers) >= len(new_numbers):
                self.numbers = new_numbers

        elif eat == 0 and bite == 1:
            new_numbers = []
            num_list = list(input_number)
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                for j in range(0, len(nums)):
                    if i == j:
                        continue
                    if nums[j] in num_list or nums[j] in self.npc_not_use_num:
                        continue
                    new_numbers.append(nums[i] + num_list[0] + nums[j])
                    new_numbers.append(nums[i] + nums[j] + num_list[0])
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                for j in range(0, len(nums)):
                    if i == j:
                        continue
                    if nums[j] in num_list or nums[j] in self.npc_not_use_num:
                        continue
                    new_numbers.append(num_list[1] + nums[i] + nums[j])
                    new_numbers.append(nums[i] + nums[j] + num_list[1])
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                for j in range(0, len(nums)):
                    if i == j:
                        continue
                    if nums[j] in num_list or nums[j] in self.npc_not_use_num:
                        continue
                    new_numbers.append(num_list[2] + nums[i] + nums[j])
                    new_numbers.append(nums[i] + num_list[2] + nums[j])
            if len(self.numbers) > len(new_numbers):
                self.numbers = new_numbers

        elif eat == 0 and bite == 2:
            new_numbers = []
            num_list = list(input_number)
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                new_numbers.append(nums[i] + num_list[0] + num_list[1])
                new_numbers.append(num_list[0] + num_list[1] + nums[i])
                new_numbers.append(num_list[0] + nums[i] + num_list[1])
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                new_numbers.append(nums[i] + num_list[1] + num_list[2])
                new_numbers.append(num_list[1] + num_list[2] + nums[i])
                new_numbers.append(num_list[1] + nums[i] + num_list[2])
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                new_numbers.append(nums[i] + num_list[0] + num_list[2])
                new_numbers.append(num_list[0] + num_list[2] + nums[i])
                new_numbers.append(num_list[0] + nums[i] + num_list[2])
            if len(self.numbers) >= len(new_numbers):
                self.numbers = new_numbers

        elif eat == 1 and bite == 1:
            new_numbers = []
            num_list = list(input_number)
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                new_numbers.append(num_list[0] + nums[i] + num_list[1])
                new_numbers.append(num_list[0] + num_list[2] + nums[i])
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                new_numbers.append(nums[i] + num_list[1] + num_list[0])
                new_numbers.append(num_list[2] + num_list[1] + nums[i])
            for i in range(0, len(nums)):
                if nums[i] in num_list or nums[i] in self.npc_not_use_num:
                    continue
                new_numbers.append(nums[i] + num_list[0] + num_list[2])
                new_numbers.append(num_list[1] + nums[i] + num_list[2])

        # 使用されている数字が確定した場合
        elif eat == 0 and bite == 3:
            # 使用している数列のみを抽出する。（今回入力した数列は外す）
            new_numbers = [n for n in self.numbers if input_number[0]  in n and input_number[1]  in n and input_number[2]  in n]
            if input_number in new_numbers:
                new_numbers.remove(input_number)
            if len(self.numbers) > len(new_numbers):
                self.numbers = new_numbers
            else:
                if input_number in self.numbers:
                    self.numbers.remove(input_number)

        elif eat == 1 and bite == 2:
            new_numbers = []
            inp = list(input_number)
            new_numbers.append(inp[0] + inp[2] + inp[1])
            new_numbers.append(inp[2] + inp[1] + inp[0])
            new_numbers.append(inp[1] + inp[0] + inp[2])
            if len(self.numbers) > len(new_numbers):
                self.numbers = new_numbers
            else:
                if input_number in self.numbers:
                    self.numbers.remove(input_number)

    def input_history(self, input_number, eat, bite):
        if self.now_player == 1:
            self.user_history.append( [input_number, eat, bite] )
        else:
            self.npc_history.append( [input_number, eat, bite] )

    def history_check(self):
        for his in self.npc_history:
            if his[0] in self.numbers:
                self.numbers.remove(his[0])

if __name__ == '__main__':
    numeron = Numeron()
    print('===================================================')
    print(f'あなたの選んだ数字：{numeron.user_set_num}')
    print(f'NPCの選んだ数字：{numeron.npc_set_num}')
    print('===================================================')
    while numeron.winner == '':
        numeron.input_num()
        numeron.now_player *= -1
        print()
