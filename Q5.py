#Q5

def Q5(s):
    if (s[0]=='.'   or    s[len(s)-1]=='.'):
        return False
    c=0
    for i in range(1,len(s)-1):
        if (s[i]=='.'):
            if (s[i+1]=='.'):
                return False
            c+=1 
    if (c>0):
        return True
    return False


print(Q5("8jdjd"))      #False
print(Q5(".8jdjd"))     #False
print(Q5("8jd..jd"))    #False
print(Q5("8jdjd."))     #True
print(Q5("8jdjd.."))    #False
print(Q5("8jdj.d."))    #True
print(Q5("8j.djd"))     #True
