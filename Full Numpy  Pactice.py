#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


array = np.array([[1,2,3,4,5],[2,4,3,1,3]]) 
array1 = np.array([[2,3,6,7,5],[2,4,3,1,3]])


# In[3]:


array


# In[4]:


np.zeros(3)


# In[5]:


np.zeros((3,2))


# In[6]:


np.zeros((3,2,5))


# In[7]:


np.full((3,2),3)


# In[8]:


np.random.rand(3,5)


# In[9]:


np.ones((2,3))


# In[10]:


np.eye(3)


# In[11]:


array.size


# In[12]:


array.shape


# In[13]:


array.dtype


# In[14]:


np.copy(array)


# In[15]:


arr2 = np.append(array,[79,54,64,65])


# In[16]:


np.append(array,[23,43,23])


# In[17]:


array


# In[18]:


np.insert(array,2,5)


# In[19]:


np.delete(array,0,axis=0)


# In[20]:


array


# In[21]:


arr2


# In[22]:


array


# In[23]:


arr2


# In[24]:


array


# In[25]:


np.delete(array,1)


# In[26]:


np.concatenate((array,array1),axis = 1)


# In[27]:


array


# In[28]:


array1


# In[29]:


np.split(array, 2, axis = 0)


# In[30]:


array1[0,2]


# In[ ]:




