from game import Game
import db
from deck import Deck
def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    user=Game()
    user.setup()
    user.guide()
    
    while True: 
            try:
                option = int(input())
                if option >=1 and option <=8:
                    break
                else:
                    print("Hãy nhập số theo menu")
            except:
                
                print ("Bạn phải nhập số")
    dem=db.get_thutulanchoi()
    if dem is None:
        dem=0
    while option !=8:
        if option==1:
            user.list_players()
            user.guide()

            option=int(input())
        if option==2:
            if user.playing==True:
                print("Bài đang chơi rồi")
            else: 
                user.add_player()
            user.guide()
            option=int(input())
        if option==3:
            if user.playing==True:
                print("Bài đang chơi rồi")
            else:
                user.remove_player()
            user.guide()
            option=int(input())
        if option==4:
            if user.playing==True:
                print("Bài đang chơi rồi")
            else:
                user.deal_card()
                dem=dem+1
                db.logs(user,dem)
                
            user.guide()
            option=int(input())
        if option==5:
            if user.playing==False:
                print("Bài chưa được chia!!!")
            else:
                user.flip_card()
                db.games(user,dem)
                
                for i in range(0,len(user.ds_nguoichoi)):
                        user.ds_nguoichoi[i].card.clear()
               
                user.deck=Deck()
                user.deck.build()
            user.guide()
            option=int(input())
        if option==6:
            db.get_last_game()
            user.guide()
            option=int(input())
        if option==7:
            db.history()
            user.guide()
            option=int(input())
        if option==8:
            break
    
if __name__ == '__main__':
    main()
