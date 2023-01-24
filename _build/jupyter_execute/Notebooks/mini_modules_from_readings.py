#!/usr/bin/env python
# coding: utf-8

# # Mini Python Modules - From Readings

# ## Here is fibo.py

# In[1]:


"""
A python module to compute, print or return Fibonacci series
"""
def fib(n): # write Fibonacci series up to n 
    a, b = 0, 1 
    while a < n: 
        print(a, end=' ') 
        a, b = b, a+b 
    print() 

def fib2(n): # return Fibonacci series up to n 
    result = [] 
    a, b = 0, 1 
    while a < n: 
        result.append(a) 
        a, b = b, a+b 
    return result

#Don't worry too much if you don't understand what's happening here:
#Uncomment if you want to save as a .py and execute from an interpreter:
#if __name__ == "__main__":
#    import sys
#    fib(int(sys.argv[1]))


# I'll test with two function calls below:

# In[2]:


fib(100)


# In[3]:


a = fib2(100)
print(a)


# In[ ]:




