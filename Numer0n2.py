import random

def duplication_check(num):
    is_duble = ( len(num) == len(set(num)) )
    is_3num = ( len(num) == 3 )
    if is_duble and is_3num:
        return True


def input_number(prompt):
    print(prompt)
    while True:
        num = input('３桁の数字を入力：')
        if duplication_check(num):
            return num
        print('再入力してください')

def eat_bite_check(player_number,cpu_number):
    eat = 0
    bite = 0
    for n, m in zip(player_number, cpu_number):
        if n == m:
            eat += 1
        elif n in cpu_number:
            bite += 1
    return eat,bite
    #return (str(eat)+ 'EAT-'+ str(bite)+ 'BITE')

def generate_number():
    return ''.join(random.sample("0123456789", 3))

def play_game():
    player_number = input_number('まず始めにあなたの番号を決めます')
    random_number = str(random.randint(1,1000))
    cpu_number = random_number

    while True:

        print('---------------------------------------------------')
        player_number = input_number('コンピューターの３桁の数字を予想してください：')
        eat, bite = eat_bite_check(player_number,cpu_number)
        print(f'結果は[{eat}EAT-{bite}BITE]でした')
        if eat == 3:
            print('あなたの勝ちです')
            return 
        

        print('コンピューターがあなたの番号を予想します')
        cpu_number = generate_number()
        print('コンピューターは'+ str(cpu_number)+ 'と予想しました')
        eat, bite = eat_bite_check(player_number,cpu_number)
        print(f'結果は[{eat}EAT-{bite}BITE]でした')
        if eat == 3:
            print('あなたの負けです')
            return

if __name__ == '__main__':
    print('ゲームを開始します')
    play_game()
    print('ゲームを終了します')



