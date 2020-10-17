#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Question No. 1


# In[19]:


print("Enter a number")
num1= int(input())
print("Enter 2nd number")
num2 = int(input())


# In[20]:


list = []
for num in range(num1, num2):
    if (num%7 == 0) & (num%5) != 0:
        list.append((num))
        print(num)
        


# In[21]:


#Question No.2


# In[22]:


print("Enter your 1st name")
first_name = input()
print("Enter your last name")
last_name = input()


# In[27]:


rev_first_name = first_name[::-1]
print(rev_first_name)
rev_last_name = last_name[::-1]
print(rev_last_name)

print(rev_first_name +" " +rev_last_name)


# In[ ]:





# In[28]:


#Question No. 3


# In[53]:


print("Enter diameter of sphere")
diameter = float(input())
radius = diameter/2
print("radius of sphere", radius)


# In[54]:


import math
volume = ((4/3)*(radius**3.0)*math.pi)
print("volume of sphere", volume)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




