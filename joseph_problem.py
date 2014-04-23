#约瑟夫问题

def yuesefu(pNum,k):   #pNum约瑟夫环的人数，k相隔多少个人就提出去
    if pNum>0:
        if k>0:
            a = [x for x in range(1,pNum)]
            del_number = k
            for i in range(pNum-1):
                print(a[del_number-1])
                del a[del_number-1]
                del_number=(del_number-1+k)%len(a)
            print('the last number is: ')
            print(a)

#yuesefu(30,8) #共30人，每间隔8个就剔除一个人
