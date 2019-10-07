class Counter(object):
    #__slots__ = ['cnt']

    def __init__(self):
        self.cnt = 0

    def count(self):
        self.cnt += 1
    
    def doublecount(self):
        self.cnt += 2
    
    def reset(self):
        self.cnt = 0
    
    def show(self):
        print(self.cnt)

    def __repr__(self):
        return str(self.cnt)

c = Counter()
c.count()
c.show()

c = Counter()
c.doublecount()
c.show()

c2 = Counter()
c2.show()

print(type(c))
print(c)
