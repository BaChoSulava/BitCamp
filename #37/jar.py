import sys

class Jar:
    def __init__(self, capacity=12, cookies=0):
        self.capacity = capacity
        self.cookies = cookies

    def deposit(self, n):
        if self.cookies + n >= self.capacity:
            raise ValueError("Cookie jar capacity exceeded")
        self.cookies += n
        return self.cookies

    def withdraw(self, n):
        if n > self.cookies:
            raise ValueError("Not enough cookies in the jar")
        self.cookies -= n
        return self.cookies
    
    def get_capacity(self):
        return self.capacity

    def get_size(self):
        return self.cookies
    
    def __str__(self):
        return "🍪" * self.cookies

jar = Jar()

jar.deposit(10)
jar.withdraw(9)
print(jar.get_size())
print(jar.__str__())
