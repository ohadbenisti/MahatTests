#Q2
import random as rd

class Box:
    def __init__(self, color, length, width, hieght):
        self.__color=color
        self.__length=length
        self.__width=width
        self.__hieght=hieght
    def GetColor(self):
        return self.__color
    def GetLength(self):
        return self.__length
    def GetWidth(self):
        return self.__width
    def GetHieght(self):
        return self.__hieght

    def SetColor(self,c):
        self.__color=c
    def SetLength(self,l):
        self.__length=l
    def SetWidth(self,w):
        self.__width=w
    def SetHieght(self,h):
        self.__hieght=h

    def StringColor(self,color):
        self.__color=color
        self.__length=10
        self.__width=10
        self.__hieght=10

        
def SmallestBox(arr):
    mc=0
    smaller=check=arr[0].GetLength()*arr[0].GetWidth()*arr[0].GetHieght()
    for i in range(1,len(arr)):
        check=arr[i].GetLength()*arr[i].GetWidth()*arr[i].GetHieght()
        if check<smaller:
            smaller=check
            mc=i
    return arr[mc].GetColor()

def Show(arr):
    for i in range(len(arr)):
        print("Box", i, ":", arr[i].GetColor(), arr[i].GetLength(),
              arr[i].GetWidth(), arr[i].GetHieght(),
              "Nefach:",
              arr[i].GetLength()*arr[i].GetWidth()*arr[i].GetHieght())
    

    
colors=["Red","Blue","Brown","Yellow","Green","Gray"]
boxes=[0]*20
for i in range(len(boxes)):
    boxes[i]=Box(colors[rd.randint(0,len(colors)-1)],rd.randint(1,40),rd.randint(1,40),rd.randint(1,40)  )


Show(boxes)
print(SmallestBox(boxes))

        
