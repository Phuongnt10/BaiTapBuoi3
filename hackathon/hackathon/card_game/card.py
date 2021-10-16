class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''

    def __init__(self,rank, suit):
        self.rank=rank
        self.suit=suit

    def __str__(self):
        '''Hiển thị lá bài'''
        return (str(self.rank) + self.suit)

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
        pass

