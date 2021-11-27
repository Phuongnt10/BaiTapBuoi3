from game import Game
import db
from deck import Deck
def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    game=Game()
    game.setup()
    game.guide()
    
    while True: 
            try:
                option = int(input())
                if option >=1 and option <=8:
                    break
                else:
                    print("Hãy nhập số theo menu")
            except:
                
                print ("Bạn phải nhập số")

    while option !=8:
        if option==1:
            game.list_players()
            game.guide()
            option=int(input())
        if option==2:
            if game.playing==True:
                print("Bài đang chơi rồi")
            else: 
                game.add_player()
            game.guide()
            option=int(input())
        if option==3:
            if game.playing==True:
                print("Bài đang chơi rồi")
            else:
                game.remove_player()
            game.guide()
            option=int(input())
        if option==4:
            if game.playing==True:
                print("Bài đang chơi rồi")
            else:
                game.deal_card()    
            game.guide()
            option=int(input())
        if option==5:
            if game.playing==False:
                print("Bài chưa được chia!!!")
            else:
                game.flip_card()
                for i in range(0,len(game.ds_nguoichoi)):
                        game.ds_nguoichoi[i].card.clear()
                game.deck=Deck()
                game.deck.build()
            game.guide()
            option=int(input())
        if option==6:
            game.get_last()
            game.guide()
            option=int(input())
        if option==7:
            game.get_history()
            game.guide()
            option=int(input())
        if option==8:
            break
    
if __name__ == '__main__':
    main()
