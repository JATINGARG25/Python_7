class Vector:
    def __init__(self,vec):
        self.vec = vec
    def __str__(self):
        return f"{self.vec[0]}i + {self.vec[1]}j + {self.vec[2]}k "

    def __len__(self):
        return len(self.vec)
    
a = Vector([1,2,3])
print(a)
print(len(a))