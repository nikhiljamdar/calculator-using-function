class addition:
    a=0
    b=0
    c=0
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def display(self):
        print("first number:"+ str(self.a))
        print("second number:"+ str(self.b))
        print("addition of two numbers:"+str(self.c))
    def calc(self):
        self.c=self.a+self.b
obj=addition(int(input("enter first number:")),int(input("enter second number:")))
obj.calc()
obj.display()