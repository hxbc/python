num1=int(raw_input('enter a number:'))
list1=range(1,num1+1)
print'before:',`list1`

i =0
while i<len(list1):
    if num1%list1[i]==0:
        del list1[i]
    i+=1


print "after:",`list1`
