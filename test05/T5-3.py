num = raw_input("enter your defen:")
numi = int(num)

s=[]


while 0<= numi <=100:
    s.append(numi)
   # print s
  #  print(numi)
  #  print(type(numi))
    if (numi) < 60:
        print("F")
    elif 60<=(numi)<=69:
        print("D")
    elif 70<=(numi)<=79:
        print("C")
    elif 80<=(numi)<=89:
        print("B")
    elif 90<=(numi)<=100:
        print("A")
    junfen=sum(s)/len(s)
    print('pingjunfen is:%f'% junfen)
    cho=raw_input('''(Q)uit \n (G)oon''')
    if cho=='Q':
        break
    elif cho=='G':
        pass

    numi=int(raw_input("enter aother num:"))

else:
    print("you have rong num!")


'''def choose(cho):
     print((Q)uit
              (G)on)
     cho=raw_input("choose you xuanze:")
     if cho=='Q':
        break
     elif cho=='G':
         numi=int(raw_input("enter aother num:"))
'''
