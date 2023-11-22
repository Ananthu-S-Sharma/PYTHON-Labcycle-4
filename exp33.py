class rectangle:
    def __init__(self,length,width):
        self.__len=length
        self.__wid=width
    def calc__area(self):
        self.__area=self.__len*self.__wid
        print("Area is :",self.__area)
        return(self.__area)
    def calc__peri(self):
        self.__peri=2*(self.__len+self.__wid)
        print("Perimeter is :",self.__peri)   
length1=int(input("Enter length of the rectangle 1:"))
width1=int(input("Enter width of the rectangle 1:"))
length2=int(input("Enter length of the rectangle 2:"))
width2=int(input("Enter width of the rectangle 2:"))
obj1 = rectangle(length1,width1)
obj2 = rectangle(length2,width2)
r1=obj1.calc__area()
r2=obj2.calc__area()
obj1.calc__peri()
obj2.calc__peri()
if r1 < r2:
    print("Rectangle Two is large")
else:
    print("Rectangle One is large")
