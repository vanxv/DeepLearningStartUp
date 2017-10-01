# -*- coding: utf-8 -*
import re
import sys
txt = open('happiness_seg.txt', 'r', encoding='utf-8')
alltxt = txt.read()
txt.close()

#把下面的变成词组，通过正式表达式
#re.split(' ',alltxt)
stxt = re.split(r'\s|\s+|[\u3002\uff1b\uff0c\uff1a\u201c\u201d\uff08\uff09\u3001\uff1f\u300a\u300b]',alltxt)
#清除空值
# for b in stxt:
#     if b == "":
#         stxt.remove(b)
#     if b == " ":
#         stxt.remove(b)
#递归的模式，变成二元数组
sn = len(stxt)
listTwotxt = []
for x in range(1,sn):
    if len(stxt[x-1]) >= 2:
        if len(stxt[x]) >= 2:
            listTwotxt.append(stxt[x-1] + ' ' + stxt[x])
txtdict={}

# for i in listTwotxt:
# 	# txtdict[i] = i
# 	if i in txtdict = True:
# 		txtdict[i] = txtdict[i] + 1
# 	else:
# 		txtdict[i] = 1

for r in listTwotxt:
    if r not in txtdict:
        txtdict[r] = 1
    else:
        txtdict[r] += 1

sortedDict = sorted(txtdict.items(), key=lambda x: x[1], reverse=True)
for i in sortedDict[:10]:
    print(i[0], ":", i[1])
