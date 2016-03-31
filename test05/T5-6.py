jisuan = raw_input("enter your jisuan shi:")
print(jisuan + "jieguoshi:")
import os
#stra=os.path.split(jisuan)

if "+" in jisuan:

    #print("+")
    str1,str2 = jisuan.split('+',1)
    jieguo = float(str1) + float(str2)
    print(jieguo)
elif "-" in jisuan:
    str1,str2 = jisuan.split('-',1)
    jieguo = float(str1) - float(str2)
    print(jieguo)
elif "*" in jisuan:
    str1,str2 = jisuan.split('*',1)
    jieguo = float(str1) * float(str2)
    print(jieguo)
elif "/" in jisuan:
    str1,str2 = jisuan.split('/',1)
    jieguo = float(str1) / float(str2)
    print(jieguo)
elif "%" in jisuan:
    str1,str2 = jisuan.split('%',1)
    jieguo = float(str1) % float(str2)
    print(jieguo)
elif "**" in jisuan:
    str1,str2 = jisuan.split('**',1)
    jieguo = float(str1) ** float(str2)
    print(jieguo)

