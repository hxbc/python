def zhuanm(numh,numm):
    x=int(numh)*60
    y=int(numm)
    print('you enter gong:%d min!'%(x+y))


def zhuanh(num1):
    """

    :rtype: object
    """
    z=int(num1)
    h=z//60
    m=z%60
    print('you have %d hour and %d min!'%(h,m))


strh=raw_input("enter hour:")
strm=raw_input("enter min:")
if int(strh)>0:zhuanm(strh,strm)
elif int(strh)==0 and int(strm)>0:zhuanh(strm)

