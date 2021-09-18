n = int(input()) 
def anagram_number(n):
    str1 = f"{n}"    
    str2 = str1[::-1] 
    if (str1 == str2):
        return True   
    else:
        return False
print (anagram_number(n)) 

##def roman_to_int(s):
  ##  pass