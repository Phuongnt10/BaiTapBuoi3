

from datetime import datetime
def day_diff(release_date,code_complete_day):
    date_format="%d/%m/%Y"
    release_date = datetime.strptime(release_date,date_format)
    date_format1="%Y/%d/%m"
    code_complete_day = datetime.strptime(code_complete_day,date_format1)
    result=release_date-code_complete_day
    return result.days

# 2
#import re
#def alpha_num(sentence):
 #   str=sentence.split()
  #  result_str=re.findall("\d+[a-zA-Z]+|[a-zA-Z]*\d+",sentence)
   # return result_str
