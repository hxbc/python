def huiba(num):
    #num1=raw_input("enter a num:")
    i=1
    num1=num
    while i<365:

        num2=num1 + num1*0.002
        i+=1
        num1=num2

    print num2,num1,num

s=huiba(100)

