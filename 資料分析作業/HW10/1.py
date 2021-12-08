
import csv

fn='csvReport.csv'
sum1=0#儲存2015年業績
sum2=0#儲存2016年業績
with open(fn) as fnFile:  #打開檔案
    file=csv.reader(fnFile) #讀取
    listfile=list(file) #把csv檔案變串列
    for i in range(1,11): #用for檢查每一列是否有2015年的業績 
        if listfile[i][1]=='2015': #如果是2015年就做累加
            sum1+=int(listfile[i][5])
        elif listfile[i][1]=='2016':
            sum2+=int(listfile[i][5])
print("Total  Revenue of 2015=%d"%(sum1)) #印出結果
print("Total  Revenue of 2016=%d"%(sum2))#印出結果