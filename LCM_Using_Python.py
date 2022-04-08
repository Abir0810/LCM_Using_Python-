#!/usr/bin/env python
# coding: utf-8

# # LCM Using Python

# In[6]:


def least_common_multiple(a,b):
    if a > b:
        greater = a
    elif b > a :
        greater = b
    while(True):
        if((greater %a ==0) and (greater % b == 0)):
            lcm=greater
            break
        greater+=1
    return lcm
a=int(input("enter first number: "))
b=int(input("enter second number: "))
print(least_common_multiple(a,b))


# In[4]:


# Python Program to find the L.C.M. of two input number

def compute_lcm(x, y):

   # choose the greater number
   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           lcm = greater
           break
       greater += 1

   return lcm

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("The L.C.M. is", compute_lcm(num1, num2))


# In[13]:


# Python program to find the L.C.M. of two input number

# This function computes GCD 
def compute_gcd(x, y):

   while(y):
       x, y = y, x % y
   return x

# This function computes LCM
def compute_lcm(x, y):
   lcm = (x*y)//compute_gcd(x,y)
   return lcm

num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))

print("The L.C.M. is", compute_lcm(num1, num2))


# In[ ]:




