#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class power:
    def _init_(self,x,n):
        self.x=x
        self.n=n
    def calculate(self):
        print(self.x**self.n)
a=int(input('x:'))
b=int(input('n:'))
power1= power(a,b)
power1.calculate( )

