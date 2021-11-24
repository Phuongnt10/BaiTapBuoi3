##Bài in sao
# n=6
# for i in range(1,n+1):
#     print (("  " * (n-i)) + ("* " * i))

# n=6
# for i in range(1,n+1):
#     end = "\n" if i < n else "" 
#     print (("  " * (n-i)) + ("* " * i),end = end)

# for i in range(0,n):
#     start = "  " * n if i > 0 else ""
#     print (start + ("* " * (n-i)) + ("  " * i))    


##Bài Đếm số

# from collections import Counter
# my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]
# c = Counter(my_list)
# print(c)


# ## Bài Đếm ngược đến XMas
# from datetime import date
# from datetime import time
# from datetime import datetime
# import time


# date_xsmas=datetime(2021, 12, 25, 00, 00, 00, 000000)
# while True:
#     now = datetime.now()
#     result_time=date_xsmas-now
#     time.sleep(5)
#     print(result_time)


# ## Bài: Unique value Dictionary

# unique_value_dict =[dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)]
# u_value = set( val for dic in unique_value_dict for val in dic.values())
# print("Tuổi duy nhất:",u_value)


# unique_value_dict= [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

# u_value = set( val for dic in unique_value_dict for val in dic.values())
# print("5 giá trị trả về duy nhất : ",u_value)



# ## Bài: Find Pair
# list_a = [3, 6, 7, 9, 11, 12]
# n_sum=18
# list_str=[]
# for i in range(len(list_a)-1) : ##range khoảng for trong 1 list range(2, 6) - chỉ lấy từ 2-5
#     a=list_a[i] ## khai báo a = từng phần tử trong list: a= 3,6,7,9...
#     for j in range(i+1,len(list_a)): ##i+ 1 vì ko thể a= b= 3 cộng 2 lần với nhau
#         b=list_a[j]
#         if a+b == n_sum:
#             c=a,b
#             list_str.append(c)
# print(list_str)