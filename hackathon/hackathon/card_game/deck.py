from card import Card
import random
class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    ranks=[2,3,4,5,6,7,8,9,1]
    suits= ['♠', '♣', '♦', '♥']

    def build(self):
        '''Tạo bộ bài'''
        # print("Tạo bộ bài nào")
        self.cards=[]
        for i in Deck.ranks:
            for j in Deck.suits:
                self.cards.append(Card(i,j))
        # for i in self.cards:
        #     print(i)    

    def shuffle_card(self):
        '''Trộn bài'''
        # print("Xem bài trộn")
        random.shuffle(self.cards)
        # for i in self.cards:
        #     print(i)

    def deal_card(self):
        '''Rút một lá bài từ bộ bài'''
        return self.cards.pop(0)
# de=Deck()
# de.build()
# de.shuffle_card()