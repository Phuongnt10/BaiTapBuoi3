from player import Player
import os
class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self.ds_nguoichoi=[]
       

    def setup(self):
        soluong=int(input("Nhập vào số lượng người chơi: "))
        for i in range(soluong):
            print("Tên người chơi thứ " + str(i+1))
            nguoichoi = input()
            self.ds_nguoichoi.append(nguoichoi)
           

    def guide(self):
        '''menu'''
        print("1.Danh sách người chơi: "+  str(len(self.ds_nguoichoi)))
        print("2.Thêm người chơi mới")
        print("3.Loại người chơi")
        ##print("4.Chia bài")
        ##print("5.Lật bài")
        ##print("6.Xem lại game vừa chơi")
        ##print("7.Xem lịch sử chơi hôm nay")
        ##print("8.Tốc biến")

    def list_players(self):
        '''danh sách ng chơi'''
        print("Danh sách người chơi:")
        for i in self.ds_nguoichoi:
            print(i)

    def add_player(self):
        '''Thêm người chơi mới'''
        print("Nhập người chơi mới: ")
        nguoichoi_moi=input()
        self.ds_nguoichoi.append(nguoichoi_moi)

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        print("Bạn muốn loại người chơi thứ mấy:")
        index_ngchoi=int(input())
        del self.ds_nguoichoi[index_ngchoi-1]

    def deal_card(self):
        '''Chia bài cho người chơi'''
        pass

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        pass

##ga=Game()
##ga.setup()
##ga.guide()
##ga.list_players()
##ga.add_player()
##ga.list_players()
##ga.remove_player()
##ga.list_players()