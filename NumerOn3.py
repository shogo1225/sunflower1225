import random
import time
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
    data = []
    player_deffence_number = input_number('まず始めにあなたの番号を決めます')
    random_number = str(random.randint(1,1000))
    cpu_deffence_number = random_number

    while True:

        print('---------------------------------------------------')
        print('あなたが当てるです')
        player_attacking_number = input_number('コンピューターの３桁の数字を予想してください：')
        eat, bite = eat_bite_check(player_attacking_number,cpu_deffence_number)
        print(f'結果は[{eat}EAT-{bite}BITE]でした')

        #データの入力
        row=[player_attacking_number,eat,bite]
        print(row)
        
        if eat == 3:
            print('あなたの勝ちです')
            return data
    
        print('コンピューターがあなたの番号を予想します')
        print('予測中')
        time.sleep(2)
        cpu_number = generate_number()
        print('コンピューターは'+ str(cpu_number)+ 'と予想しました')
        eat, bite = eat_bite_check(player_deffence_number,cpu_number)
        print(f'結果は[{eat}EAT-{bite}BITE]でした')

        #データの入力
        row=[cpu_number,eat,bite]
        print(row)

        if eat == 3:
            print('あなたの負けです')
            return data


import csv
import sys



def save(file_path, data):
    with open(file_path, 'w') as f:
        writer = csv.writer(f, lineterminator='\n') # 改行コード（\n）を指定しておく
        writer.writerows(data) # 2次元配列も書き込める


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("please input number")
        exit()
    
    folder = "./CSV"
    file_name = sys.argv[1]
    file_path = folder + "/" + file_name

    print('ゲームを開始します')
    data = play_game()
    print('セーブします')
    save(file_path, data)
    print('ゲームを終了します')
