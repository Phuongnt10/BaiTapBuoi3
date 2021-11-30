from deck import Deck
from player import Player
import os
import sys
import db
class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self.ds_nguoichoi=[]
        self.deck=Deck()
        self.deck.build()
        self.playing=False

    def setup(self):
        print("Mời nhập số lượng người chơi:")
        while True: 
            try:
                sl_nguoichoi = int(input())
                if sl_nguoichoi >=2 and sl_nguoichoi <=12:
                    break
                else:
                    print("Số lượng người chơi tối thiểu là 2 tối đa là 12")
            except:
                
                print ("Dữ liệu không hợp lệ, mời bạn nhập lại")
                print (">")
           
        
        for i in range(1,sl_nguoichoi+1):
           nguoichoi=input("Nhập tên người chơi thứ "+ str(i)+": ")
           self.ds_nguoichoi.append(Player(nguoichoi))
        return self.ds_nguoichoi
           

    def guide(self):
        '''menu'''
        print("1.Danh sách người chơi: "+  str(len(self.ds_nguoichoi)))
        print("2.Thêm người chơi mới")
        print("3.Loại người chơi")
        print("4.Chia bài")
        print("5.Lật bài")
        print("6.Xem lại game vừa chơi")
        print("7.Xem lịch sử chơi hôm nay")
        print("8.Tốc biến")

    def list_players(self):
        '''danh sách ng chơi'''
        print("Danh sách người chơi:")
        for i in self.ds_nguoichoi:
            print(i)

    def add_player(self):
        '''Thêm người chơi mới'''
        print("Nhập SỐ LƯỢNG người chơi mới: ")
        nguoichoi_moi= int (input())
        if (nguoichoi_moi+len(self.ds_nguoichoi))>12:
            print ("Không thêm được người chơi do đã quá số lượng người được chơi")
        else:
            for i in range(nguoichoi_moi):
                print ("Nhập tên người chơi thứ", len(self.ds_nguoichoi)+1)
                n_player= input()
                self.ds_nguoichoi.append(Player(n_player))
            print ("Thêm người chơi thành công")    
    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        print("Bạn muốn loại người chơi thứ mấy:")
        index_ngchoi=int(input())
        
        if len(self.ds_nguoichoi)>2:
            if index_ngchoi <= len(self.ds_nguoichoi):
                del self.ds_nguoichoi[index_ngchoi-1]
                print ("Xóa thành công")
            else:
                print('Không tìm thấy người chơi!')
        else:
            print ("Không thể xóa do số lượng người chơi đã là tối thiểu")

    def deal_card(self):
        '''Chia bài cho người chơi'''
        self.deck.shuffle_card()
        for j in range (0,3):
            for i in self.ds_nguoichoi:
                i.add_card(self.deck.deal_card()) 
        print("-----!----")        
        print("Chia xong rồi bạn nhé")        
        print("-----!----")
        self.playing=True

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        name_win=None
        for Player in self.ds_nguoichoi:
            print("-----!----")
            print ("Người chơi: ",Player)
            
            Player.flip_card() 
            if name_win==None:
                name_win=Player
            else:
                if name_win.point == Player.point:
                    if Player.biggest_card > name_win.biggest_card:
                        name_win = Player
                elif Player.point > name_win.point:
                        name_win = Player
            print("-----!----")
            print ("Số điểm của", Player.name, "là:", Player.point)
            print ("Lá bài có giá trị lớn nhất", Player.biggest_card)
            
        print(f'Bạn chiến thắng là:{name_win.name}')
        print("-----!----")
        self.playing=False
        rdb= db.games(name_win.name)
        for Player in self.ds_nguoichoi:
            card1=""
            for i in Player.card:
                card1 += str(i)
            db.logs(rdb, Player.name,card1,Player.point,Player.biggest_card )
        
    def get_last(self):
        print("-----!----")
        print("Ván bài vừa chơi:")
        last_game, players = db.get_last_game()
        print(last_game['play_at'])
        print()
        for p in players:
            print(f'Bài của {p["player"]}')
            print(
                f'Bộ bài: {p["cards"]} Điểm: {p["point"]} Lá bài lớn nhất: {p["biggest_card"]}')
            print()
        print(f'Người chơi chiến thắng: {last_game["winner"]}')
    def get_history(self):
        total_game, records = db.history()
        print("-----!----")
        print(f'Hôm nay đã chơi: {total_game} ván bài')
        for r in records:
            print(f'{r["player"]:6} thắng {r["game_won"]} ván')

