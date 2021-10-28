
def anagram_number(n):
    str1 = f"{n}"    
    str2 = str1[::-1] 
    if (str1 == str2):
        return True   
    else:
        return False


def roman_to_int(s):
    
    romans = {'I': 1,'V': 5,'X': 10,'L': 50,'C': 100,'D': 500,'M': 1000}
    result = 0
    i = 0
    while i < len(s):
        value = romans[s[i]]
        if i < len(s) - 1:
            next = romans[s[i + 1]]
            if value < next:
                result += next - value
                i += 1
            else:
                result += value
        else:
            result += value
        i += 1
    return result