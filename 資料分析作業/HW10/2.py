
import json
import csv
fn='preview.json'
fn1='preview.csv'
with open(fn) as fileobj:
    data=json.load(fileobj)#取得json
    with open(fn1,'w') as csvfile:
        fields=['sno','sna','tot']
        dicWriter=csv.writer((csvfile),delimiter='\t',)#以空格隔開
        for line in data:
            dicWriter.writerow([line['sno'],line['sna'],line['tot']])#寫入csv
