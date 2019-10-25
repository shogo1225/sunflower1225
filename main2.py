from agent2 import NumeronAgent, NumeronHumanAgent


class Game(object):
    """
    Numeron対戦用クラス
    """

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.nof_turns = 1

    def main(self):
        self.nof_turns = 1
        is_over = False
        while True:
            print('---------- Turn {} ----------'.format(self.nof_turns))
            print('---- pleyer1\'s turn ----')
            is_over = self.player1.action(self.player2)
            if is_over:
                return None
            print('---- pleyer2\'s turn ----')
            is_over = self.player2.action(self.player1)
            if is_over:
                return None
            self.nof_turns += 1



def PlayOneGame():
    player1 = NumeronHumanAgent()
    player2 = NumeronAgent()
      
    game = Game(player1, player2)
    game.main()
    nof_turns = game.nof_turns

    del player1,player2,game

    return nof_turns

if __name__ == '__main__':
    nof_turns_list = []
    for i in range(0,100):
        nof_turns = PlayOneGame()
        nof_turns_list.append(nof_turns)
    
    ave = sum(nof_turns_list) /len(nof_turns_list)
    print('平均ターン数は'+ str(ave) + 'です')
    