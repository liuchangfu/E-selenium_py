class Count():
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b


if __name__=="__main__":
    c=Count(3,2)
    print(c.add())
    print(c.sub())

