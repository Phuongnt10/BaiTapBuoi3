##Bài in sao
print(" Print Star1")
int_so= input('Nhập độ dài cần in ')
if int_so.isnumeric():
    for i in range(1,int(int_so)): 
        s=i*'*'
        space=(int(int_so)-i)*" "
        print(space,s) 
else:
    print("Không đúng định dạng số nguyên")

print(" Print Star2")    
n= int(input('Nhập độ dài cần in '))
for i in range(1, n):
    s = n - i ##đếm khoảng trắng để đẩy vào
    k = (s)* " "

    print(k,(i) * '*') ##in khoảng trắng và sao

for i in range(n, 0, -1): ## bắt đầu từ n nhảy dần về 0 bước nhảy 1

    if i==n:  ## điều kiện in dòng giữa 2 tam giác
       k = (-i) * ' '
       print(k, end=' ')
       print((2*i) * '*') ## nhân đôi sao
    else:
       k = (n) * ' '
  
       print(k,(i) * '*')


##Bài Đếm số
my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
number_list={
10:my_list.count(10),
21:my_list.count(21),
40:my_list.count(40),
52:my_list.count(52),
1:my_list.count(1),
2:my_list.count(2),
11:my_list.count(11),
25:my_list.count(25),
24:my_list.count(24),
60:my_list.count(60)
}
number_list

## Bài Đếm ngược đến XMas
from datetime import date
from datetime import time
from datetime import datetime
import time


date_xsmas=datetime(2021, 12, 25, 00, 00, 00, 000000)
while True:
    now = datetime.now()
    result_time=date_xsmas-now
    time.sleep(5)
    print(result_time)


## Bài: Unique value Dictionary

print("VD1")
unique_value_dict= dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)

dict2=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
list_t=[]
for i in unique_value_dict:
    if list_t.count(unique_value_dict[i])==0:
        list_t.append(unique_value_dict[i])
list_t.sort()        
print("Unique value Dictionary VD1 is: ",list_t)

print("VD2")
list_t1=[]
for j in range(0, len(dict2)):
    a=list(dict2[j].values())
    if a in list_t1:
      continue
    else:
      list_t1.append(a)
      
print("Unique value Dictionary VD2 is: ",list_t1)



## Bài: Find Pair
list_a = [3, 6, 7, 9, 11, 12]
n_sum=18
list_str=[]
for i in range(len(list_a)-1) : ##range khoảng for trong 1 list range(2, 6) - chỉ lấy từ 2-5
    a=list_a[i] ## khai báo a = từng phần tử trong list: a= 3,6,7,9...
    for j in range(i+1,len(list_a)): ##i+ 1 vì ko thể a= b= 3 cộng 2 lần với nhau
        b=list_a[j]
        if a+b == n_sum:
            c=a,b
            list_str.append(c)
print(list_str)