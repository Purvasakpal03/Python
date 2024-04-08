#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("hello")


# In[2]:


5*2


# In[2]:


for i in range(1,5):
    for j in range(1,i+1 ):
        print("*",end="")
    print()


# In[48]:


for i in range(1,5):
    for space in range(4,i,-1):
        print(" ",end="")
    for j in range(1,i+1 ):
        print("*",end="")
    print()


# In[3]:


for i in range(1,5):
    for j in range(1,i+1 ):
        print(i,end="")
    print()


# In[45]:


for i in range(1,6):
    for j in range(5,i-1,-1 ):
        print("*",end="")
    print()


# In[58]:


for i in range(1,5):
    for space in range(4,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()


# In[1]:


for i in range(1,6):
    for space in range(1,i+1):
        print(" ",end="")
    for j in range(5,i-1,-1):
        print("* ",end="")
    print()


# In[62]:


for i in range(5,0,-1):
    for space in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("* ",end="")
    print()


# In[60]:


for i in range(1,6):
    for space in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("A ",end="")
    print()
    


# In[46]:


for i in range(7,0,-1):
    for j in range(1,i+1):
        print(i,end="")
    print()
    
''("")


# In[ ]:





# In[51]:


for i in range(5,0,-1):
#     for j in range(1,i+1,1 ):
    for j in range(1,7-i):
        print("*",end="")
    print()


# In[62]:


for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print("*",end="")
    print()


# In[ ]:




