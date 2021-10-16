from game import Game
def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    game = Game() 
    game.setup()
    game.guide()
    chon = int(input())

    while True :
        if(chon==1):
            game.list_players()
        if(chon==2):
            game.add_player()
        if(chon==3):
            game.remove_player() 
        game.guide()
        chon = int(input())
    print("Dừng")

if __name__ == '__main__':
    main()
