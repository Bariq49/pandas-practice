#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv('FMCG.csv')
df.head()


# In[3]:


ProfitList = df['total_profit'].to_list()
MonthList = df['month_number'].to_list()
FaceCream = df['facecream'].to_list()


# In[ ]:





# In[4]:


plt.plot(MonthList, ProfitList)
plt.title("Company profit per month")
plt.xlabel("Month Number")
plt.ylabel("Profit in Units")
plt.xticks(MonthList)
plt.yticks([100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000])
plt.show()


# In[5]:


plt.plot(MonthList, ProfitList, linestyle = '--', color = 'r', 
         marker = 'o', markerfacecolor = 'k', linewidth = 3, label = "Profit data of last year")
plt.title("Company profit per month")
plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.xticks(MonthList)
plt.legend(loc = 'lower right')
plt.yticks([100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000])
plt.show()


# In[6]:


plt.plot(MonthList, ProfitList, "ro--", markerfacecolor = 'k', linewidth = 3, label = "Profit data of last year")
plt.title("Company profit per month")
plt.xlabel("Month Number")
plt.ylabel("Sold units number")
plt.xticks(MonthList)
plt.legend(loc = 'lower right')
plt.yticks([100000, 150000, 200000, 250000, 300000, 350000, 400000, 450000, 500000])
plt.show()


# In[7]:


df.head(3)


# In[8]:


FaceCream = df['facecream'].to_list()
FaceWash = df['facewash'].to_list()
ToothPaste = df['toothpaste'].to_list()
BathingSoap = df['bathingsoap'].to_list()
Shampoo = df['shampoo'].to_list()
Moisturizer = df['moisturizer'].to_list()


# In[9]:


plt.plot(MonthList, FaceCream, marker = 'o', linestyle = '-', linewidth = 3, label = "Face Cream Sales Data")
plt.plot(MonthList, FaceWash, "o-", linewidth = 3, label = "Face Wash Sales Data")
plt.plot(MonthList, ToothPaste, "o-", linewidth = 3, label = "Tooth Paste Sales Data")
plt.plot(MonthList, BathingSoap, "o-", linewidth = 3, label = "BathingSoap Sales Data")
plt.plot(MonthList, Shampoo, "o-", linewidth = 3, label = "Shampoo Sales Data")
plt.plot(MonthList, Moisturizer, "o-", linewidth = 3, label = "Moisturizer Sales Data")

plt.title("Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Sales units in number")
plt.xticks(MonthList)
plt.legend(loc = 'upper left')
# plt.yticks()
plt.show()


# In[10]:


df.head()


# In[11]:


MonthList = df['month_number'].to_list()
ToothPaste = df['toothpaste'].to_list()


# In[12]:


plt.scatter(MonthList, ToothPaste, label = "Tooth paste Sales data")
plt.legend(loc = 'upper left')
plt.title("Tooth paste sales data")
plt.grid(True, linestyle = "dashed", linewidth = 1)
plt.xticks(MonthList)
plt.show()


# In[13]:


df.head()


# In[14]:


FaceCream = np.array(df['facecream'])
FaceWash = np.array(df['facewash'])
MonthList = np.array(df['month_number'])


# In[15]:


FaceCream-2


# In[16]:


# FaceCream = df['facecream'].to_list()


# In[17]:


# [ i-2 for i in FaceCream]

# list = []
# for i in FaceCream:
#     list.append(i-2)
# list


# In[18]:


plt.bar(MonthList-0.25, FaceCream, width = 0.25, label = "Face Cream Sales data", align = 'edge')
plt.bar(MonthList+0.25, FaceWash, width = -0.25, label = "Face Wash Sales data", align = 'edge')
plt.xticks(MonthList)
plt.legend(loc = 'upper left')
plt.grid(True, linestyle = 'dashed', linewidth = 1)
plt.show()


# In[19]:




