A = [7, 8, 9, 2, 10, 9, 9, 9, 9, 4, 5, 6, 1, 5, 6, 7, 8, 6, 1,10] 
def do_mean():
    x=len(A)
    y=sum(A)
    result=y/x
    print("mean(A):",result,end = ' ')
def do_median():
    lst_sort=sorted(A)
    x= int(len(lst_sort)/2)
    if len(lst_sort)%2==0:
        result=(lst_sort[x] + lst_sort [x-1])/2
        print("median(A):",result,end = ' ')
    else:
        print("median(A):",lst_sort[x],end = ' ') 
def do_mode():
    b = []
    c= []
    for i in range(len(A)-1): 
        b.append(A.count(A[i]))
    list_kq=[]    
    for i in range(len(b)-1):
        if b[i] == max(b):
            c.append(A[i])
    print('mode(A):',c[0])
do_mean()
do_median()
do_mode() 


print("Cách 1 dùng nhiều hàm build in")
s = "Hello World! 123"
result_dict={}
def countkt1(s):
    count_upper = 0
    count_lower = 0
    count_text=0
    count_digit=0
    for c in s:
        if c.isupper():
            count_upper += 1
        if c.islower():
            count_lower += 1
        if c.isalpha():
            count_text +=1    
        if  c.isdigit():
            count_digit +=1
    result_dict={
        "LETTERS":count_text,
        "CASE":{"UPPER CASE":count_upper, "LOWER CASE":count_lower},
        "DIGITS":count_digit
    }
    print(result_dict)
countkt1(s)      
print("Cách 2 dùng 1 hàm build in")   
s = "Hello World! 123"
def countkt2(s):
    count_upper1 = 0
    count_lower1 = 0
    count_text1 = 0
    count_digit1 = 0
    result_dict1={}
    for i in s:
        k=ord(i)
        if k>=48 and k <=57:
            count_digit1 += 1
        if k>=65 and k <=90:
            count_upper1 += 1
         
        if k>=97 and k<=122:
            count_lower1 += 1 
        
        if k>=65 and k <=122:
            count_text1 += 1
           
    result_dict1={
            "LETTERS":count_text1,
            "CASE":{"UPPER CASE":count_upper1, "LOWER CASE":count_lower1},
            "DIGITS":count_digit1}
    print(result_dict1)        
      
countkt2(s)