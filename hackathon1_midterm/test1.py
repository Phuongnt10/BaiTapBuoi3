str1 = "Emma25 is Data scientist50 and AI Expert 2dad"
list2=[]

def alpha_num(sentence):
    sentence=sentence.split()
    for i in sentence:
        if i.isalpha() == False and i.isalnum()==True:
            list2.append(i)
    return list2

print("- Easy 2\nOutput : ",alpha_num(str1),"\n")