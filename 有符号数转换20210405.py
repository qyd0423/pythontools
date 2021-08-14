import sys
import math
import string

#需要改进
'''判断表达该数，最大需要几位，目前最低只支持INT8'''
def max_exp(exp):
    if exp > 0 and exp < 9 :
        max_value = pow(2,8)
    elif exp > 8 and exp <  13:
        max_value = pow(2,12)
    elif exp >12 and exp <17:
        max_value = pow(2,16)
    else:
        print("error")
    return max_value

def is_hex(s):
    hex_digits = set(string.hexdigits)
     # if s is long, then it is faster to check against a set
    return all(c in hex_digits for c in s)

def hex2dec_int():
    tempt = ">>>"
    print("请依次输入16进制数和增益")
    value  = input(f"十六进制{tempt}")

    ishex = is_hex(value)
    while ishex != True :
        print("输入的16进制数有误，请重新输入")
        value  = input(f"十六进制{tempt}")
        ishex = is_hex(value)
    cofe= int(input(f"放大倍数{tempt}"))
    mul = round(cofe/10)

    result = 0
    newresult = 0
    c = int(value, 16)
    c = bin(int(value, 16))

    lengh = len(c)-2
    sign = c[2:3]

    index = math.ceil(lengh)
    max_int = pow(2,index-1)-1
    
    if sign == '0':
         bin_c = int(c)
    else:
        bin_c = "0" + c[3:]
        bin_c = int(bin_c,2)-1
        bin_c = bin_c - max_int 

    if mul == 0 :
        newresult = bin_c
    else:
        newresult = round(bin_c/cofe, mul)
    print( newresult)

def dec2hex_int():
    tempt =">>>"
    print("请依次输入10进制数和增益")
    value  = input(f"10进制数{tempt}")
    cofe    = input(f"放大倍数{tempt}")
    
    value_src= float(value)*float(cofe)
    iszero = value_src - int(value_src)
    while iszero != 0:
        print("输入的放大倍数不对，请重新输入")
        cofe    = input(f"放大倍数{tempt}")
        value_src= float(value)*float(cofe)

    value_src = int(value_src)
    if value_src > 0:
        print("0x" + hex(value_src)[2:].upper())
    else:
        value_dst = abs(value_src)
        exp = math.log(value_dst,2)
        exp = math.ceil(exp)
        max_value = max_exp(exp)
        value_dst = max_value - value_dst
        print("十进制数是:",value_dst)
        print("结果是:",hex(value_dst).upper())
        print('''\n注释：
        如果是INT4，就去除前面的F
        如果是INT16，就在前面补F，补到4个数，以此类推'''
        )
    
if __name__ == "__main__":
    while True:
        tempt = ">>>"
        print("==========================")
        index = input(f'''欢迎使用有符号数的数值转化工具
10进制转化为16进制，请输入1
16进制转化为10进制，请输入0\n{tempt}''')
        if index == '0':
            hex2dec_int()
        elif index == '1' :
            dec2hex_int()
        else:
            print("ERROR: 输入的指令不对，请重新输入")
