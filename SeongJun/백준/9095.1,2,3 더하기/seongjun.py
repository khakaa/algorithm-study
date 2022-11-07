time = int(input())
hap = [0,1,2,4,7]+[0]*7
array=[]
for i in range(time):
    num=int(input())
    for j in range(4,num+1):
        hap[j]=hap[j-1]+hap[j-2]+hap[j-3]
    print(hap[num])