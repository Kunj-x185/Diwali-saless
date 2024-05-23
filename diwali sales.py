#!/usr/bin/env python
# coding: utf-8

# # Project on Diwali Sales Analysis

# In[4]:


import numpy as nu


# In[5]:


import pandas as pd
import matplotlib.pyplot as plt # visualizing data
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[8]:


# import csv file
df = pd.read_csv(r'C:\Users\kunj\Downloads\Python_Diwali_Sales_Analysis\Diwali Sales Data.csv', encoding= 'unicode_escape')
#to avoid encoding error, use 'unicode_escape'
# we used 'df' here bcz we are storing that file in df


# In[9]:


df.shape


# In[6]:


df.head(10)


# In[14]:


df.info() #used for data cleaning 


# In[17]:


df.drop (['Status','unnamed1'],axis = 1, inplace=True) #to delete column status and unnamed and here axis means whole vertical row
#and inplace means to execute whatever we have written


# In[18]:


df.info()


# In[19]:


pd.isnull(df) #to check null values and false means not null


# In[20]:


pd.isnull(df).sum()


# In[23]:


df.shape


# In[25]:


#to drop null values by using fun. 'dropna'
df.dropna(inplace=True)


# In[28]:


pd.isnull(df).sum()


# In[33]:


#to change data type
df['Amount']= df['Amount'].astype(int)


# In[35]:


df['Amount'].dtype


# In[37]:


df.columns #to check columns


# In[43]:


#rename column
df.rename(columns={'Marital_Status':'Shadii'})


# In[45]:


df.info()


# In[47]:


df.describe()
# describe () method give the description of the data in dataFrame (like mean, std etc)


# In[49]:


#to get description of a particular column 
df[['Age','Orders','Amount']].describe() 


# In[50]:


#data cleaning ends here ...... now we will learn about data analysis


# In[14]:


df.columns


# # Gender

# In[ ]:


# analysis on the basis of Gender 

ax=sns.countplot(x='Gender',data=df)

for bars in ax.containers: #to see values we use this
    ax.bar_label(bars)


# In[15]:


sales_gen= df.groupby(['Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending= False)

sns.barplot(x='Gender',y='Amount', data= sales_gen)


# From above graph we can see that most of the buyers are female and even the purchasing power of females are greater than man

# #  Age
# 

# In[14]:


df.columns


# In[21]:


ax=sns.countplot(data=df, x= 'Age Group', hue='Gender')
#hue is used to view more exactly like in this we can see male and female data seperately

for bars in ax.containers:
    ax.bar_label(bars)  


# In[42]:


#total amount vs age group

sales_age= df.groupby(['Age Group'], as_index=False)['Amount'].sum().sort_values(by='Amount',ascending= False)

sns.barplot(x='Age Group',y='Amount', data= sales_age)


# In[23]:


# from above graph we can see that most of the buyers are of age between 26-35 years


# # State

# In[25]:


df.columns


# In[53]:


#total no. of orders from top 10 states

state_sales=df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(15,5)})
sns.barplot(data=state_sales, x='State',y='Orders')


# In[57]:


#OR

state_sales=df.groupby(['State'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10) #head(10) shows top 10 

plt.figure(figsize=(15, 5))

sns.barplot(data=state_sales, x='State',y='Orders')


# From above graph we can see that most of the orders are from UP,Mahrastra and Karnatka respectively.

# # Martial status

# In[60]:


ax = sns.countplot(data = df, x = 'Marital_Status')

sns.set(rc={'figure.figsize':(10,5)})
for bars in ax.containers:
    ax.bar_label(bars)
    


# In[62]:


sales_state = df.groupby(['Marital_Status', 'Gender'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(6,5)})
sns.barplot(data = sales_state, x = 'Marital_Status',y= 'Amount', hue='Gender')


# From above graphs we can see that most of the buyers are married (women) and they have high purchasing power

# ### Occupation

# In[67]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Occupation')

for bars in ax.containers:
    ax.bar_label(bars)


# In[69]:


sales_state = df.groupby(['Occupation'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Occupation',y= 'Amount')


# From above graphs we can see that most of the buyers are working in IT, Healthcare and Aviation sector

# ### Product Category

# In[71]:


sns.set(rc={'figure.figsize':(20,5)})
ax = sns.countplot(data = df, x = 'Product_Category')

for bars in ax.containers:
    ax.bar_label(bars)


# In[73]:


sales_state = df.groupby(['Product_Category'], as_index=False)['Amount'].sum().sort_values(by='Amount', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_Category',y= 'Amount')


# From above graphs we can see that most of the sold products are from Food, Clothing and Electronics category

# In[75]:


sales_state = df.groupby(['Product_ID'], as_index=False)['Orders'].sum().sort_values(by='Orders', ascending=False).head(10)

sns.set(rc={'figure.figsize':(20,5)})
sns.barplot(data = sales_state, x = 'Product_ID',y= 'Orders')


# In[77]:


# top 10 most sold products (same thing as above)

fig1, ax1 = plt.subplots(figsize=(12,7))
df.groupby('Product_ID')['Orders'].sum().nlargest(10).sort_values(ascending=False).plot(kind='bar')


# ## Conclusion:
# 

# Married women age group 26-35 yrs from UP,  Maharastra and Karnataka working in IT, Healthcare and Aviation are more likely 
# to buy products from Food, Clothing and Electronics category

# ThanK you!

# In[ ]:




