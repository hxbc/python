def sushu(num):
    count=num/2
    while count>1:
        if num % count ==0:
            print('%d is not sushu!',num)
            break
            count-=1
        else:
            print("%d is sushu!",num)
            break


sushu(int(raw_input("enter a num:")))
