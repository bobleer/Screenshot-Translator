#!/usr/bin/env python

cptlet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
listtl = '¢—-=@#$%^*'
last = 'BoB'
lastcheck = '.!?~\n'
with open('/Users/bob/ocr.txt', 'r') as f:
    for i in f.readlines()[:-1]:
        if i != '\n':
            i = i[-1:]+i[:-2]+i[-2:-1].replace('-','')
            if (i[1] not in cptlet or last not in lastcheck) and i[1] not in listtl:
                i = ' '+i[1:]
                if last == 'BoB':
                    i = i[1:]
        last = i[-1]
        with open('/Users/bob/ocr-new.txt', 'a') as x:
            x.write(i)