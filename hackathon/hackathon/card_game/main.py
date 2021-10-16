from game import Game
def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    game = Game() 
    game.setup()
    game.guide()
    chon = int(input())

    while chon != 8 :
        if(chon==1):
            game.list_players()
        if(chon==2):
            game.add_player()
        if(chon==3):
            game.remove_player()
        if(chon==4):
            game.deal_card()
        game.guide()
        chon = int(input())
    print("END GAME")

if __name__ == '__main__':
    main()
