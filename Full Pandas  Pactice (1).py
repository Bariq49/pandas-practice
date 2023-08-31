#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv('world_population.csv', index_col='Rank')


# In[3]:


df.head()


# In[4]:


df.sort_index()


# In[5]:


df.tail()


# In[6]:


display(df)


# In[7]:


pd.set_option('display.max.rows', None)
pd.set_option('display.max.columns',None)


# In[8]:


df


# In[9]:


df.info()


# In[10]:


df.shape


# In[11]:


df[['Country/Territory', 'CCA3']]


# In[12]:


df.count


# In[13]:


df.columns


# In[14]:


df.loc[23]


# In[15]:


df.iloc[1:10 , [1,5, 6, 7]] 


# In[16]:


df.loc[1:10 , ['CCA3', '2022 Population', 'Country/Territory']]


# In[17]:


df.set_index('2022 Population')


# In[18]:


df


# In[19]:


df.sort_values('2022 Population' , ascending=False)


# In[20]:


high_population = (df['2022 Population'] > 218541211)
df[high_population]


# In[21]:


new = df.loc[high_population]
new.sort_values('2022 Population', ascending=False)


# In[22]:


df[df['Capital'].str.contains('Beijing')]


# In[23]:


df.drop(columns=['Capital'])


# In[24]:


df


# In[25]:


df.drop(index=3)


# In[26]:


df.sort_values(by = ['Rank','Capital'], ascending=True)


# In[27]:


df.sort_index()


# In[28]:


df.median()


# In[29]:


df['2022 Population'].median()


# In[30]:


df.describe()


# In[31]:


df['2022 Population'].value_counts(normalize=True)


# In[32]:


df.groupby(['2022 Population'])


# In[33]:


df.agg


# In[34]:


df[df['Country/Territory'].str.contains('Zimbabwe')]


# In[35]:


df.filter(items= ['CCA3','Capital'],axis= 1)


# In[36]:


df[['2022 Population','Country/Territory']].max()


# In[37]:


max_pop = df['2022 Population'].max()
max_pop


# In[38]:


gb = df.groupby('2022 Population').mean()
gb


# In[39]:


df.groupby(['2022 Population','2010 Population']).agg({'1970 Population':['mean','max','min']})


# In[40]:


df["2022 Population"].agg(['mean','max','min'])


# In[41]:


df.replace('Kabul','NAN')


# In[42]:


df.isna()


# In[ ]:




