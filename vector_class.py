# https://www.codewars.com/kata/526dad7f8c0eb5c4640000a4/train/python

# If you try to add, subtract, or dot two vectors with different lengths, you must throw an error!


class Vector():
    
    def __init__(self, vect):
        self.vect = vect
        self.len = len(vect)

    def add(self, b):
        if self.__compare_size(b):
            return Vector([self.vect[i] + b.vect[i] for i in range(self.len)])
        else:
            raise Exception("Cannot add two vector of different size")

    def subtract(self, b):
        if self.__compare_size(b):
            return Vector([self.vect[i] - b.vect[i] for i in range(self.len)])
        else:
            raise Exception("Cannot add two vector of different size")

    def dot(self, b):
        if self.__compare_size(b):
            return sum([self.vect[i] * b.vect[i] for i in range(self.len)])
        else:
            raise Exception("Cannot add two vector of different size")

    def norm(self):
        return (sum([el**2 for el in self.vect]) ** 0.5)

    def __str__(self):
        return f'({",".join([str(el) for el in self.vect])})'
    
    def equals(self, b):
        return self.vect == b.vect

    def __compare_size(self, b):
        return self.len == b.len
    

v1 = Vector([1, 2, 3])
v2 = Vector([3, 4, 5])

print(v1.add(v2))
print(v1.subtract(v2))
print(v1.dot(v2))
print(v1.norm())
print(v1)

v3 = Vector([1, 2, 3])
v4 = Vector([1, 2, 3, 5])

print((v1.add(v2).equals(Vector([4, 6]))))
print((v1.add(v2).equals(Vector([4, 6, 8]))))