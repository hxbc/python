listnum=['zero','one','two','three','four','five','six','seven','eight','nine','ten']

num1=raw_input('enter a num 0 to 1000:')
list1=list(num1)

li=[]
for i in range(0,len(list1)):
    num2=listnum[int(list1[i])]
    li.append(num2)
    str1='-'.join(li)
print str1




'''import re
str1=re.compile(' ')
str2=str1.sub('-',li)
print str2'''


'''l=len(list1)
i=0
list2=[]
while i<l:
    num2=list1[i]
    i+=1
    list2.append(num2)

print l
print num2
print list2

print list1'''