def convert2Binary(num:int)->str:
    result=""
    while num>0:
        if num%2==1 :
            result+='1'
            num=num//2
        else:
            result+='0'
            num=num//2
    result=result[::-1]
    return result
# print(convert2Binary(13))

def convert2Decimal(num:str)->int:
        num=str(num)
        decinum=0
        power=0
        index=len(num)-1
        while index>=0:
            d=int(num[index])*(2**power)
            decinum+=d
            index-=1
            power+=1
        return decinum
print(convert2Decimal(1101))


