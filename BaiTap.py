{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "source": [
    "##For/While loop và Dictionary/Tuple/Set - Print Star"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 169,
   "source": [
    "int_so= input('Nhập độ dài cần in ')\r\n",
    "if int_so.isnumeric():\r\n",
    "    for i in range(1,int(int_so)): \r\n",
    "        s=i*'*'\r\n",
    "        space=(int(int_so)-i)*\" \"\r\n",
    "        print(space,s) \r\n",
    "else:\r\n",
    "    print(\"Không đúng định dạng số nguyên\")"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "      *\n",
      "     **\n",
      "    ***\n",
      "   ****\n",
      "  *****\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 170,
   "source": [
    "n= int(input('Nhập độ dài cần in '))\r\n",
    "for i in range(1, n):\r\n",
    "    s = n - i ##đếm khoảng trắng để đẩy vào\r\n",
    "    k = (s)* \" \"\r\n",
    "\r\n",
    "    print(k,(i) * '*') ##in khoảng trắng và sao\r\n",
    "\r\n",
    "for i in range(n, 0, -1): ## bắt đầu từ n nhảy dần về 0 bước nhảy 1\r\n",
    "\r\n",
    "    if i==n:  ## điều kiện in dòng giữa 2 tam giác\r\n",
    "       k = (-i) * ' '\r\n",
    "       print(k, end=' ')\r\n",
    "       print((2*i) * '*') ## nhân đôi sao\r\n",
    "    else:\r\n",
    "       k = (n) * ' '\r\n",
    "  \r\n",
    "       print(k,(i) * '*')\r\n",
    "    "
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "       *\n",
      "      **\n",
      "     ***\n",
      "    ****\n",
      "   *****\n",
      "  ******\n",
      " **************\n",
      "        ******\n",
      "        *****\n",
      "        ****\n",
      "        ***\n",
      "        **\n",
      "        *\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "source": [
    "'''Viết chương trình trả ra từ điển với key là các số trong list, value là số lần xuất hiện của số trong list\r\n",
    "my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]\r\n",
    "Trả ra\r\n",
    "{10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}'''\r\n",
    "my_list = [10, 21, 21, 40, 40, 52, 52, 1, 1, 2, 2, 2, 2, 11, 11, 11, 11, 25, 24, 24, 60, 40]\r\n",
    "number_list={\r\n",
    "10:my_list.count(10),\r\n",
    "21:my_list.count(21),\r\n",
    "40:my_list.count(40),\r\n",
    "52:my_list.count(52),\r\n",
    "1:my_list.count(1),\r\n",
    "2:my_list.count(2),\r\n",
    "11:my_list.count(11),\r\n",
    "25:my_list.count(25),\r\n",
    "24:my_list.count(24),\r\n",
    "60:my_list.count(60)\r\n",
    "}\r\n",
    "number_list"
   ],
   "outputs": [
    {
     "output_type": "execute_result",
     "data": {
      "text/plain": [
       "{10: 1, 21: 2, 40: 3, 52: 2, 1: 2, 2: 4, 11: 4, 25: 1, 24: 2, 60: 1}"
      ]
     },
     "metadata": {},
     "execution_count": 24
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "source": [
    "'''Cho list A chứa các số nguyên đã sắp xếp theo thứ tự tăng dần.\r\n",
    "Vd A = [3, 6, 7, 9, 11, 12] và một số nguyên sum. Tìm tất cả các cặp số (a,b) trong mảng A có tổng bằng sum\r\n",
    "vd ở đây nếu sum = 18 thì kết quả là [(7,11), (6,12)]. Nếu không có cặp số nào thỏa mãn thì in ra list rỗng []'''\r\n",
    "\r\n",
    "list_a = [3, 6, 7, 9, 11, 12]\r\n",
    "n_sum=18\r\n",
    "list_str=[]\r\n",
    "for i in range(len(list_a)-1) :\r\n",
    "    a=list_a[i]\r\n",
    "    for j in range(i+1,len(list_a)):\r\n",
    "        b=list_a[j]\r\n",
    "        if a+b == n_sum:\r\n",
    "            c=a,b\r\n",
    "            list_str.append(c)\r\n",
    "print(list_str)"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "[(6, 12), (7, 11)]\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "source": [
    "'''Cho một list gồm 1 hoặc nhiều từ điển (Dictionary). Viết chương trình để trả ra tập hợp tất cả các giá trị (values) duy nhất trong tất cả danh sách các từ điển trên.\r\n",
    "\r\n",
    "[VD1]: Trường hợp dưới đây danh sách đầu vào có 1 từ điển map tên người vào tuổi của họ. Trả ra set các tuổi duy nhất.'''\r\n",
    "unique_value_dict= dict(Trang=38, Thu=38, Ngoc=27, Thanh=26, Yen=25, Hang=22, Thuy=22)\r\n",
    "list_t=[]\r\n",
    "for i in unique_value_dict:\r\n",
    "    if list_t.count(unique_value_dict[i])==0:\r\n",
    "        list_t.append(unique_value_dict[i])\r\n",
    "list_t.sort()        \r\n",
    "print(list_t)\r\n",
    "\r\n"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "[22, 25, 26, 27, 38]\n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 132,
   "source": [
    "from datetime import date\r\n",
    "from datetime import time\r\n",
    "from datetime import datetime\r\n",
    "import time"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 134,
   "source": [
    "'''Viết chương trình in ra thời gian đếm ngược đến XMas 2021 sau mỗi khoảng thời gian nhất định.\r\n",
    "\r\n",
    "vd in ra sau mỗi 5s:\r\n",
    "\r\n",
    "Countdown to Xmas 2021: 112 days, 11:47:01.339588\r\n",
    "Countdown to Xmas 2021: 112 days, 11:46:56.324008\r\n",
    "Countdown to Xmas 2021: 112 days, 11:46:51.310473'''\r\n",
    "\r\n",
    "\r\n",
    "\r\n",
    "date_xsmas=datetime(2021, 12, 25, 00, 00, 00, 000000)\r\n",
    "\r\n",
    "while now<date_xsmas:\r\n",
    "    now = datetime.now()\r\n",
    "    result_time=date_xsmas-now\r\n",
    "    time.sleep(5)\r\n",
    "    print(result_time)"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "110 days, 3:12:23.294641\n",
      "110 days, 3:12:18.288340\n"
     ]
    },
    {
     "output_type": "error",
     "ename": "KeyboardInterrupt",
     "evalue": "",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\PHUONG~1\\AppData\\Local\\Temp/ipykernel_25876/2225734337.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m     14\u001b[0m     \u001b[0mnow\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m     15\u001b[0m     \u001b[0mresult_time\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0mdate_xsmas\u001b[0m\u001b[1;33m-\u001b[0m\u001b[0mnow\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m---> 16\u001b[1;33m     \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m     17\u001b[0m     \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mresult_time\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mKeyboardInterrupt\u001b[0m: "
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 141,
   "source": [
    "n = int(input(\"Nhập số n: \"))\r\n",
    "for i in range (0,n+1) :\r\n",
    "    for j in range (0,n-i) :\r\n",
    "        print (end= \"  \")\r\n",
    "    if i == n: i=(n)*2\r\n",
    "    for j in range (0, i):\r\n",
    "        print ('* ', end=\"\")\r\n",
    "    print (\"\\r\")\r\n",
    "for i in range (n-1, 0, -1) :\r\n",
    "    print(n*2*' ', end='')\r\n",
    "    for k in range (0,i):\r\n",
    "        print(\"* \", end='')\r\n",
    "    print(\"\\r\")"
   ],
   "outputs": [
    {
     "output_type": "stream",
     "name": "stdout",
     "text": [
      "              \n",
      "            * \n",
      "          * * \n",
      "        * * * \n",
      "      * * * * \n",
      "    * * * * * \n",
      "  * * * * * * \n",
      "* * * * * * * * * * * * * * \n",
      "              * * * * * * \n",
      "              * * * * * \n",
      "              * * * * \n",
      "              * * * \n",
      "              * * \n",
      "              * \n"
     ]
    }
   ],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 166,
   "source": [
    "from datetime import datetime"
   ],
   "outputs": [],
   "metadata": {}
  },
  {
   "cell_type": "code",
   "execution_count": 165,
   "source": [
    "\r\n",
    "a = datetime (2021,12,24,23,59,59,999999)\r\n",
    "b = datetime.now()\r\n",
    "c=a-b\r\n",
    "while c > 0:\r\n",
    "  print(\"Countdown to Xmas 2021:\" ,c)\r\n",
    "time.sleep(5)"
   ],
   "outputs": [
    {
     "output_type": "error",
     "ename": "TypeError",
     "evalue": "'>' not supported between instances of 'datetime.timedelta' and 'int'",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mTypeError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32mC:\\Users\\PHUONG~1\\AppData\\Local\\Temp/ipykernel_25876/3186335801.py\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mb\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mdatetime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mnow\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      3\u001b[0m \u001b[0mc\u001b[0m\u001b[1;33m=\u001b[0m\u001b[0ma\u001b[0m\u001b[1;33m-\u001b[0m\u001b[0mb\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 4\u001b[1;33m \u001b[1;32mwhile\u001b[0m \u001b[0mc\u001b[0m \u001b[1;33m>\u001b[0m \u001b[1;36m0\u001b[0m\u001b[1;33m:\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      5\u001b[0m   \u001b[0mprint\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m\"Countdown to Xmas 2021:\"\u001b[0m \u001b[1;33m,\u001b[0m\u001b[0mc\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      6\u001b[0m \u001b[0mtime\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0msleep\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;36m5\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mTypeError\u001b[0m: '>' not supported between instances of 'datetime.timedelta' and 'int'"
     ]
    }
   ],
   "metadata": {}
  }
 ],
 "metadata": {
  "orig_nbformat": 4,
  "language_info": {
   "name": "python",
   "version": "3.7.8",
   "mimetype": "text/x-python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "pygments_lexer": "ipython3",
   "nbconvert_exporter": "python",
   "file_extension": ".py"
  },
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.7.8 64-bit"
  },
  "interpreter": {
   "hash": "04635d289a519a1410467dd0afb0db42f9184808881ca68b2eb5a687a20a5a94"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}