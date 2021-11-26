from card import Card
class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self,name):  # dễ
        self.name=name
        self.card=[]
    def __str__(self):
        return self.name    

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        diem=0
        for i in self.card:
            diem+=i.rank
        return diem % 10    
    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        return max(self.card)

    def add_card(self,card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        self.card.append(card)

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self.card.clear()

    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
        for i in self.card:
            print(i)
            
    def __gt__(self,other):
        '''Player có lá bài lớn nhất'''
        if self.point > other.point:
            return True
        if self.point == other.point:
            if self.biggest_card > other.biggest_card:
                return True
            else:
                return False
        return False    
        
    def ghep_card(self):
         chuoi=""
         for i in self.card:
           chuoi=i.__str__()+chuoi
         return chuoi

