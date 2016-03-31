'''def ch1(num):
    s = []
    for i in range(4):
        s.append(str(num %256))
        num /= 256
        return '.'.join(s[::-1])
        print s

ch1(123465789)'''



'''ip=raw_input("shuru ip:")
num1=ip.split('.')
print num1

a=int(num1[0])
b=int(num1[1])
c=int(num1[2])
d=int(num1[3])

print a,b,c,d

m=((a*256+b)*256+c)*256+d
print m'''

#2887057931
num2=raw_input("shuru zhengshu:")
str2=bin(int(num2))
a=str2[2:]
print a

stra=a[0:8]
strb=a[8:16]
strc=a[16:24]
strd=a[24:32]

print 'ip is :%d.%d.%d.%d'%(int(stra,2),int(strb,2),int(strc,2),int(strd,2))
print stra,strb,strc,strd




'''print bin(int(num2))
print int('10101100000101010000001000001011',2)
str1='10101100000101010000001000001011'
print len(str1)

#print int(num2,2)
'''
