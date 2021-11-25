

from datetime import datetime
def day_diff(release_date,code_complete_day):
    d1 = datetime.strptime(release_date, "%d/%m/%Y")
    d2 = datetime.strptime(code_complete_day, "%Y-%d-%m")
    return abs((d2 - d1).days)

# 2

import re
def alpha_num(sentence):
    reg = "\w+\d+"  
    regStr = re.findall(reg, sentence)
    return(regStr)