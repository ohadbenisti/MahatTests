
#Q4

def Q4(a):
    if (len(a)%2==0):                  #Check if the array is odd
        return False
    if (a[len(a)//2]!=0):              #The middle member in the array
        return False
    for i in range(len(a)//2+1):       #Run untill the middle
        if (a[i]//10>0 or a[i]<0):     #Check if it single-digit and possitive
            return False
    i+=1                               #Skip the middle member
    for i in range(i,len(a)):          #Check the second half of array
        if (a[i]//10==0):              #If NOT single-digit
            return False
    return True


a=[1,2,3,3,0,77,665,443,900000]     
print(Q4(a))                            #True
a=[1,2,3,0,33,22,11]
print(Q4(a))                            #True
print(Q4([1,5,44,0,44,33,22]))          #False
print(Q4([1,5,4,9,44,33,22]))           #False
print(Q4([1,5,4,0,4,33,22]))            #False
print(Q4([1,5,4,6,5,0,4,33,2992]))      #False
print(Q4([1,5,4,6,5,0,4,33,2]))         #False
print(Q4([1,5,4,6,0,58,664,33,29]))     #True
  
