import math

def modify_M_N():
    tempt = ">>>"
    M = input(f"请输入你想修改的接入电池模组个数{tempt}")
    N = input(f"请输入你想修改的可均衡电池模组个数{tempt}")
    while int(M) < int(N):
        print(f"电池模组个数不能小于可均衡模组个数，请重新输入")
        M = input(f"请输入你想修改的接入电池模组个数{tempt}")
        N = input(f"请输入你想修改的可均衡电池模组个数{tempt}")

    return int(M),int(N)

def modify_ksys():
    ksys = 1
    return ksys

def soh(packsoh,M,N):
    sum = 0
    packsoh = packsoh[:M]
    packsoh.sort()
    packsoh.reverse()

   # print(packsoh)
    #print(packsoh[0:N+1])
    #print(packsoh[N+1:M])

    if N == 0 :
        sum = 0
        packsoh_n = packsoh[M-1]
    elif N + 1 == M:
        packsoh_n = packsoh[0]
        for i in range(1,M):
            sum += packsoh[i]
    else:
        packsoh_n = packsoh[N+1]
        for i in range(N+1,M):
            sum+=packsoh[i]
    #print("剩余的N个求和sum = ",sum)
    #print(f"找出特征值第{N}+1个SOH:",packsoh_n)
    soh=((M-N)*packsoh_n + sum)/M
    if soh > 100:
        print(f"ERROR: 电池簇SOH超过范围为{math.floor(soh)}%")
        soh = 100   
    #print(soh)
    print(f"电池簇SOH为{math.floor(soh)}%")


def soc(packsoc,packsoh,M,N):
    Q1_product = 0
    Q2_product = 0
    packsoc = packsoc[:M]
    packsoh = packsoh[:M]
    product1 = map(lambda a,b: a*b,packsoc,packsoh)
    product2 = map(lambda a,b: (100-a)*b,packsoc,packsoh)
      
    Q1_product = list(product1)
    Q2_product = list(product2)
    Q1_product.sort()
    Q2_product.sort()

#    for i in range(M):
#        print(i+1,Q1_product[i])
#    for i in range(M):
  #      print(i+1,Q2_product[i])
   
    Q1 = Q1_product[N]
    Q2 = Q2_product[N]
    if Q1 + Q2 == 0:
        soc = 0
    else:
        soc = Q1/(Q1+Q2)*100
    print(f"电池簇SOC为{math.floor(soc)}%")

def soe(packsoe,M,N):
    sum = 0
    packsoe = packsoe[0:M]
    packsoe.sort()
    #print(packsoe)
#    for i in range(M):
#       print(i+1,packsoe[i])
    soe_n = packsoe[N-1]
    for i in range(N,M):
       sum+=packsoe[i]
    soe = modify_ksys()*(soe_n*N + sum)/M
    if soe > 100:
        print(f"ERROR: 电池簇SOE超过范围为{math.floor(soe)}%")
        soe = 100
  
    print(f"电池簇SOE为{math.floor(soe)}%")
              
if __name__ == "__main__":
    while True:
        tempt = ">>>"
        print("==========================")
        packsoc  =[57,63,88,36,83,30, 53,30,87,24,12,15,73,79,97,55,44,89,79,47,36]
        packsoh =[85,98,72,49,59,67,100,98,80,56,90,66,83,93,68,11,23,57,49,80,94]
        packsoe =[85,98,72,49,59,67,100,98,80,56,90,66,83,93,68,11,23,57,49,80,94]
        index = input(f'''
直接按回车继续，输入1修改M与N{tempt}''')      
        if index == '1':
            M,N = modify_M_N()
        else:
            M=21
            N=10
        soc(packsoc,packsoh,M,N)
        soh(packsoh,M,N)
        soe(packsoe,M,N)
