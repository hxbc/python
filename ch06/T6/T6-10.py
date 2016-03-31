import string
def zhuanhuan(str1):
    d=string.uppercase
    x=string.lowercase
    sc=''
    for c in str1:
        if c in x:
            sc += c.upper()
        elif c in d:

            sc += c.lower()
        else:
            sc +=c

    print sc


str2=raw_input('enter some:')

print str2.swapcase()
#zhuanhuan(str2)
