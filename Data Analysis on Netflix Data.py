#!/usr/bin/env python
# coding: utf-8

# In[24]:


import pandas as pd
import seaborn as sns
data=pd.read_csv(r"C:\\Users\Rishabh\Downloads\8. Netflix Dataset.csv")
data


# In[8]:


data.head(5)


# In[9]:


data.shape


# In[10]:


data.size


# In[11]:


data.columns


# In[12]:


data.dtypes


# In[13]:


data.info()


# In[14]:


# Is there any Duplicate record in this dataset? if yes remove.


# In[16]:


data[data.duplicated()]


# In[21]:


data.drop_duplicates()


# In[22]:


data.shape


# In[ ]:


data.drop_duplicates(inplace=True)


# In[23]:


#is there any null value


# In[26]:


data.isnull().sum()


# In[28]:


sns.heatmap(data.isnull()) #showing in heatmap


# #1-for "house of the cards",what is the show id and who is Director of this show?

# In[30]:


data.head(2)


# In[36]:


data[data['Title'].isin(["House of Cards"])]


# #2- In which year highest no. of the TV shows & movies releases? 

# In[38]:


data.dtypes


# In[44]:


data['Date_N'] = pd.to_datetime(data['Release_Date'])


# In[45]:


data.head()


# In[46]:


data.dtypes


# In[50]:


data['Date_N'].dt.year.value_counts()


# In[51]:


data['Date_N'].dt.year.value_counts().plot(kind='bar')


# #3- How many Movies and TV shows in the dataset?

# In[169]:


data.head(1)


# In[54]:


data.groupby("Category").Category.count()


# In[55]:


data.groupby("Category").Category.count().plot(kind='bar')


# #4 Show the movies released in year 2000

# In[61]:


data['Year']= data['Date_N'].dt.year


# In[62]:


data.head(2)


# In[81]:


data[ (data['Category']=='Movie') & (data['Year']==2000)]


# In[82]:


data[ (data['Category']=='Movie') & (data['Year']==2020)]  #filtering


# #5- Show the TV Shows released on India

# In[89]:


data[(data['Country']=='India')& (data['Category']=="TV Show")]['Title']


# #6- Show top 10 directors who gave the highest no. of tv shows and movies to Netflix?
# 

# In[168]:


data.head(1)


# In[150]:


data["Director"].value_counts().head(10)


# #7 Show the records where category is movies and type is comedy or country is United Kingdom

# In[99]:


data.head(1)


# In[105]:


data[(data["Category"]=="Movie") & (data['Type']=='Comedies') | (data['Country']=='United Kingdom')]


# #8 In how many movie Tom Cruise was cast

# In[107]:


data.head(1)


# In[120]:


data_new=data.dropna()


# In[167]:


data_new.head(1)


# In[124]:


data_new[data_new["Cast"].str.contains("Tom Cruise")]


# #9 what are rating defined by netflix

# In[127]:


data['Rating'].nunique()        #count


# In[128]:


data['Rating'].unique()         #exact result


# #10 how many tv shows got R rating after 2018?

# In[134]:


data[(data['Category']=="TV Show") & (data["Rating"]=="R") & (data['Year']>2018)] 


# #11-what is max duration of movies/show?
# 

# In[137]:


data['Duration'].nunique()


# In[139]:


data.Duration.dtypes


# In[143]:


data[['Min','Unit']] = data['Duration'].str.split(' ',expand = True)


# In[152]:


data.head(1)


# In[145]:


data['Min'].max()


# In[157]:


data.head(2)


# In[166]:


data['Type'].value_counts().head(10).plot(kind='bar')

