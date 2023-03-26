class Number:
    def __init__(self,num):
        self.num = num
    def __add__(self,num2):
        print("Lets add")
        return self.num+num2.num
    def __mul__(self,num2):
        print("Lets multiply")
        return self.num*num2.num

    def __str__(self): 
        return f"Decimal Number:{self.num}"
    
    def __len__(self):
        return 1

n1 = Number(4)
n2 = Number(5)
sum = n1+n2
mul = n1*n2
print (mul)
print(sum)
print(n1)
print(len(n1))
