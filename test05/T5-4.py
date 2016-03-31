def runnian(nian):
    a=int(nian)
    if a%4 == 0 != a%100 or a%4 == 0 == a%100:
        return 1
    else:
        return 0


nianfen = raw_input("shu ru nian fen:")

yorn = runnian(nianfen)

if int(yorn)==1:
       print(nianfen + "nian is runnian!")
else:
    print(nianfen + "nian is not runnian!")

i=2016
int(i)
while True:
    if (i%400==0 and i%4 == 0 != i%100) or (i%4 == 0 == i%100 and i%400==0):
        print("next zhengrunnian is:" + str(i))
        break
    else:
        i=i+1





