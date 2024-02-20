def brothers(a,b):
    if (a%10!=b%10):
        return False
    a=str(a)
    b=str(b)
    if (a[0]!=b[0]):
        return False
    return True


def brothers2(a,b):
    if (a%10!=b%10):
        return False
    while (a>9):
        a=a//10
    while(a>9):
        b=b//10
    if(a!=b):
        return False
    return True



print(brothers(101,11))

print(brothers(100984094872,1992300320232))

print(brothers(101999999999999,119))

print(brothers(40593310,4115555))

