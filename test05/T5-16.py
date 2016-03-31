blance=input("Enter opening balance:")
payment=input("ENter monthly payment:")
print("Pymt:"+"      "+"Paid"+"           "+"Balance" )
print("------"+"     "+"------"+"        "+"----------" )
i=0
paid=0
while blance-payment>0 and paid>=0:
    if i==0:
        payment=0.00
    else:


        print(str(i) + "         " + "$"+str(payment) + "              " + "$" + str(blance))

    i+=1
    paid=blance-payment
    print paid






