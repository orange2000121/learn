def bubble(nums):#氣泡排序
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if(nums[i]>nums[j]):
                temp=nums[i]
                nums[i]=nums[j]
                nums[j]=temp
    return nums

def average(nums):#計算平均數
    addup=0
    for i in range(10):
        addup+=nums[i]
    ave=addup/10
    return ave

def middle(nums):#計算中位數
    return (nums[5]+nums[6])/2

def mode(nums):#計算眾數
    count_dir={}
    #統計每個數的量
    for i in nums:
        if(str(i) in count_dir):
            count_dir[str(i)]+=1
        else:
            count_dir[str(i)]=1
    max=0
    maxseat=0
    for i in count_dir:
        if(max<count_dir[i]):
            max=count_dir[i]
            maxseat=i
    if(max>1):
        return maxseat
    else:
        return '沒有眾數'
nums=[]
for i in range(10):
    nums.append(int(input('輸入數字')))
    print()

nums=bubble(nums)
print('排序:',nums)
print('中位數:',middle(nums))
print('平均數:',average(nums))
print('眾數:',mode(nums))