#Q1

z=0
ez=0

for i in range (10):
    num=int(input("Enter a number:"))
    if num>99 and num<1000:
        a=num
        b=0
        while (a>0):
            b+=a%10
            a//=10
        print("The sum of this number is: " , b)

    if (num%2==0):
        z+=1
    else:
        ez+=1
        
print()
print()
print()
print("The quantity of even numbers is: " , z)
print("The quantity of odd numbers is: " , ez)


