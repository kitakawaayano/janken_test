from source import player
from source import computer
from source import janken_judge

def main():
   """3回戦のじゃんけんゲームを行う関数"""
   # hands = ['グー', 'チョキ', 'パー']
   player_win = 0
   computer_win = 0
   round = 1
   
   while round <= 3:
    player_win, computer_win, round = rounds(player_win, computer_win, round)
   final_round(player_win, computer_win)
   
   
def rounds(player_win, computer_win, round):
    print(f"-----ラウンド {round} -----")
    computer_hand = computer.computer_pon()
    player_hand = player.player_pon()
    result = janken_judge.judge(computer_hand,player_hand)

    print(f"あなたの手:{player_hand}")
    print(f"コンピューターの手:{computer_hand}")
    print("")  
    if result == 'draw':
      print("あいこです！ 再度対決！")
    else:
      round += 1 
      if result == 'player_win':
        player_win +=1
        print("あなたの勝ちです！")
      else:
        computer_win +=1
        print("コンピューターの勝ちです！")            
    print("")
    return player_win, computer_win, round

def final_round(player_win, computer_win):
   print("【最終結果】")
   print(f"あなた:{player_win}勝")
   print(f"コンピュータ:{computer_win}勝")
   if player_win >= computer_win:
     print("あなたの総合勝利です！")
     return "あなたの総合勝利です！"
   else:
      print("コンピュータの総合勝利です！")
      return "コンピュータの総合勝利です！"

if __name__ == '__main__':
   main()