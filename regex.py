import re
# list_resutl=[]
t= open('animal_code.google.com',encoding='UTF-8')
tf=t.read()
find_add=re.findall("GET (.*\.jpg).*/(.\..\..\..)",tf)
find_dup=set (find_add)
for i in find_dup:
    join="http://"+i[1]+i[0]
    print(join)