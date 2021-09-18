# 1 # Easy [1] Day different:
##Viết hàm day_diff() nhận vào ngày phải release sản phẩm và ngày đội dev viết xong code.
#  Tính số ngày mà team test có để test sản phẩm (= release_date - code_complete_day). 
# Lưu ý, ngày release sản phẩm sẽ ở định dạng 19/12/2021 còn ngày code_complete có định dạng 2021-17-05

from datetime import datetime

rd="19/12/2021"
date_format="%d/%m/%Y"
release_date = datetime.strptime(rd,date_format)
cd= "2021/17/5"
date_format1="%Y/%d/%m"
code_complete_day = datetime.strptime(cd,date_format1)
def day_diff(release_date,code_complete_day):
    result=release_date-code_complete_day
    print("số ngày mà team test có để test sản phẩm: ",result)
day_diff(release_date,code_complete_day)
# 2
import re
sentence = "Emma25 is Data scientist50 and AI Expert 2gild"
def alpha_num(sentence):
    str=sentence.split()
    result_str=re.findall("\d+[a-zA-Z]+|[a-zA-Z]*\d+",sentence)
    print(result_str)
alpha_num(sentence)