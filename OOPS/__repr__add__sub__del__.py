class Complex:
        def __init__(self,r,i):
                self.real=r
                self.imag=i
        def __repr__(self):
                return "{} i{}".format(self.real,self.imag)
        def __add__(self,c):
                return Complex(self.real+c.real,self.imag+c.imag)
        def __del__(self):
                print('Destructor')
c1=Complex(10,20)
c2=Complex(20,30)
c3=c1+c2
print('c1 : ',c1,'\nc2 : ',c2,'\nc3(c1+c2) : ',c3)
c3+=c1
print('c3(c3+=1) : ',c3)
del c1
del c2
del c3
'''
output:
c1 :  10 i20 
c2 :  20 i30 
c3(c1+c2) :  30 i50
Destructor
c3(c3+=1) :  40 i70
Destructor
Destructor
Destructor
'''
