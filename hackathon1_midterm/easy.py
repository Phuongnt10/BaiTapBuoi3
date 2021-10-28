

from datetime import datetime
def day_diff(release_date,code_complete_day):
    date_format="%d/%m/%Y"
    release_date = datetime.strptime(release_date,date_format)
    date_format1="%Y/%d/%m"
    code_complete_day = datetime.strptime(code_complete_day,date_format1)
    result=release_date-code_complete_day
    return result.days

# 2
import re
def alpha_num(sentence):
    str1 = "Emma25 is Data scientist50 and AI Expert 2dad"
    list2=[]

    def alpha_num(sentence):
        sentence=sentence.split()
        for i in sentence:
            if i.isalpha() == False and i.isalnum()==True:
                list2.append(i)
        return list2

    print("- Easy 2\nOutput : ",alpha_num(str1),"\n")
