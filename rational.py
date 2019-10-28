class Q(object):
    def __init__(self,a,b):
        self.a=a
        self.b=b
        def __repr__(self,a,b=1):
            self.a=a
             self.b = b
  def __repr__(self):
      if self.b == 1 :
          return str(self.a)
          return f`{self.a}/{self.b}`

          def add(self,q):
              a = self.a
              b = self.b
              c = q . a
              d = q . b
              return Q(a*d+b*c,b*d)        




q1 = new Q(1,2)
q1.a => 1
q2.b => 2
print (q1 + q2)

