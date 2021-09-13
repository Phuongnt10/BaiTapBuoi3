print("Bài 1 đảo từ")
def handle_str():
    org_str = 'tHE fOX iS cOMING fOR tHE cHICKEN'
    a= org_str.split()
    b=a[::-1]
    c=' '.join(b)
    print("Chuỗi gốc",org_str)
    print("Chuỗi đã xử lý",c.swapcase())
handle_str()    

print("Bài 2 cách 1")
def sort_diem():
    list_of_tuples = ([(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]) 
    midterm1 = lambda point: point[0]
    midterm2 = lambda point: point[1]
    endterm = lambda point: point[2]
    result=sorted(list_of_tuples, key = endterm)
    print("Danh sách gốc: ", list_of_tuples)
    print("Danh sách đã sắp xếp: ",result)
sort_diem()    


print("Bài 2 cách 2")
def sort_diem1():
    list_of_tuples = ([(1, 2, 5), (9, 1, 2), (6, 4, 4), (3, 2, 3), (10, 2, 1)]) 
    print(sorted(list_of_tuples, key = operator.itemgetter(2)))
sort_diem1()    