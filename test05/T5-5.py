ennum= raw_input("enter a num < 1 :")#输入金额小于1
zonge = 100*float(ennum)#总美分

num25 = int(zonge)//25#换多少个25美分
num_25 = int(zonge)%25#换完25剩余多少美分


num10 = num_25//10  #剩余的换多少10美分
num_10 = num_25%10  #换完还剩多少美分

num1=num_10//1

print("you can huan :"),
print()
print (zonge,num25,num_25,num10,num_10,num1)