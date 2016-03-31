print ("1:make TextFile")
print ("2:read TextFile")
choose_num = int(raw_input("choose the num :"))



if choose_num == 1:
    import os
    ls = os.linesep

    while True:
          filename = raw_input("enter a file name:")

          if os.path.exists(filename):
                  print("***ERROR:'%s'is alarry cunzai" % filename)
          else:
                  break

    all = []
    print ("\n enter lines 'over'to out! \n ")

    while True:
        enter = raw_input("===>")
        if enter == "over":
            break
        else:
            all.append(enter)

    fojb = open(filename,'w')
    fojb.writelines(["%s%s" %(x,ls) for x in all])
    fojb.close()
    print('new file' + filename + 'is creat!')


elif choose_num == 2:

    filenameR = raw_input("enter what open file name: ")
    print("\n")

    fojbf = open(filenameR, 'r')
    if True:
        for eachLine in fojbf:
            print(eachLine),
    else:
        print("error: '%s' is not found!" % filenameR)

else:
    print ('you have a cuowu num!')
