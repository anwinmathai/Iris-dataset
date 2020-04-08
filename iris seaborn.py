#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 15:42:34 2020

@author: Anwin Mathai
"""
#!/usr/bin/env python
# coding: utf-8

# In[1]:

#importing seaborn for visualisation and setting its style.
import seaborn as sns
sns.set()
sns.set(style="darkgrid")


# In[2]:

#Loading data
iris = sns.load_dataset("iris")
print(iris.head())


# In[6]:

#Knowing the dimension of the data
iris.shape


# In[7]:

#Barplot of different variables.
sns.barplot(x="species", y="sepal_length", data=iris[:150])


# In[8]:


sns.barplot(x="species", y="sepal_width", data=iris[:150])


# In[9]:


sns.barplot(x="species", y="petal_length", data=iris[:150])


# In[10]:


sns.barplot(x="species", y="petal_width", data=iris[:150])


# In[12]:


# scatter plot sepals
sns.relplot(x="sepal_length", y="sepal_width", data=iris[:150], kind="scatter");


# In[13]:


# scatter plot sepals
sns.relplot(x="petal_length", y="petal_width", data=iris[:150], kind="scatter");


# Hue semantic

# In[15]:


#To know the difference between the sepal length and sepal widths in each species
sns.relplot(x="sepal_length", y="sepal_width", hue="species",data=iris[:150]);


# In[16]:


#To know the difference between the petal length and petal widths in each species
sns.relplot(x="petal_length", y="petal_width", hue="species",data=iris[:150]);


# In[18]:

#catplot on the sepal length and width
sns.catplot(x="sepal_length", y="sepal_width",kind="point",data=iris)


# In[19]:

#catplot on the petal length and width
sns.catplot(x="petal_length", y="petal_width",kind="point",data=iris)


# In[20]:
#Relations between all four parameters of the data with species of iris


sns.pairplot(iris, hue='species', height=2.5);


# In[ ]:



