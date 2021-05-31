#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib.font_manager as fm #한글 폰트 사용하기 위한 라이브러리


# In[2]:


get_ipython().run_line_magic('matplotlib', 'nbagg')


# In[3]:


df = pd.read_csv("china.txt", delimiter="\t")


# In[4]:


df.head() #수집한 파일의 데이터프레임


# In[5]:


df.columns


# In[6]:


df = df.rename(columns={'국적별외국인 관광객.9': '중국 합계','국적별외국인 관광객.10': '중국인 남성', '국적별외국인 관광객.11': '중국인 여성'})


# In[7]:


df = df.rename(columns={'국적별외국인 관광객.3': '일본 합계','국적별외국인 관광객.4': '일본인 남성', '국적별외국인 관광객.5': '일본인 여성'})


# In[8]:


df = df.rename(columns={'국적별외국인 관광객.6': '미국 합계','국적별외국인 관광객.7': '미국인 남성', '국적별외국인 관광객.8': '미국인 여성'})


# In[9]:


df.head()


# In[10]:


df1 = df.drop([0,1])


# In[11]:


df1.index=['19.03','19.04','19.05','19.06','19.07','19.08','19.09','19.10','19.11','19.12','20.01','20.02','20.03']


# In[12]:


df1.head(2)


# In[13]:


data1 = df1.loc[:,['중국인 남성','중국인 여성','중국 합계']]


# In[14]:


data2 = df1.loc[:,['일본인 남성','일본인 여성','일본 합계']]


# In[15]:


data3 = df1.loc[:,['미국인 남성','미국인 여성','미국 합계']]


# In[16]:


data1


# In[17]:


data2


# In[18]:


data3


# In[19]:


data1['중국인 남성'] =data1['중국인 남성'].str.replace(",","").astype("float")
data1['중국인 여성'] =data1['중국인 여성'].str.replace(",","").astype("float")
data1['중국 합계'] =data1['중국 합계'].str.replace(",","").astype("float")


# In[20]:


data1.head(2)


# In[21]:


data2['일본인 남성'] =data2['일본인 남성'].str.replace(",","").astype("float")
data2['일본인 여성'] =data2['일본인 여성'].str.replace(",","").astype("float")
data2['일본 합계'] =data2['일본 합계'].str.replace(",","").astype("float")


# In[22]:


data3['미국인 남성'] =data3['미국인 남성'].str.replace(",","").astype("float")
data3['미국인 여성'] =data3['미국인 여성'].str.replace(",","").astype("float")
data3['미국 합계'] =data3['미국 합계'].str.replace(",","").astype("float")


# In[23]:


fm.get_fontconfig_fonts()
font_location = 'C:/Windows/Fonts/HANDotum.ttf'
font_name = fm.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
## title, label 등에 한글을 사용하기 위함


# In[24]:


"""
ax = plt.subplot(111)
ax.bar(np.arange(len(data1.index))-0.2, data1['중국인 남성'], width=0.2, color='b', align='center',label='male')
ax.bar(np.arange(len(data1.index)), data1['중국인 여성'], width=0.2, color='r', align='center',label='female')
ax.bar(np.arange(len(data1.index))+0.2, data1['중국 합계'], width=0.2, color='g', align='center',label='total')
plt.legend()
plt.xticks(np.arange(len(data1.index)),data1.index,rotation=30)
plt.xlabel("기간")
plt.title("중국인 방문객 현황")

plt.show()
"""


# In[25]:


"""
ax = plt.subplot(111)
ax.bar(np.arange(len(data2.index))-0.2, data2['일본인 남성'], width=0.2, color='olive', align='center',label='male')
ax.bar(np.arange(len(data2.index)), data2['일본인 여성'], width=0.2, color='pink', align='center',label='female')
ax.bar(np.arange(len(data2.index))+0.2, data2['일본 합계'], width=0.2, color='yellow', align='center',label='total')
plt.legend()
plt.xticks(np.arange(len(data2.index)),data2.index,rotation=30)
plt.xlabel("기간")
plt.title("일본인 방문객 현황")

plt.show()
"""


# In[26]:


ax = plt.subplot(111)
ax.bar(np.arange(len(data3.index))-0.2, data3['미국인 남성'], width=0.2, color='chocolate', align='center',label='male')
ax.bar(np.arange(len(data3.index)), data3['미국인 여성'], width=0.2, color='c', align='center',label='female')
ax.bar(np.arange(len(data3.index))+0.2, data3['미국 합계'], width=0.2, color='brown', align='center',label='total')
plt.legend()
plt.xticks(np.arange(len(data3.index)),data3.index,rotation=30)
plt.xlabel("기간")
plt.title("미국인 방문객 현황")

plt.show()


# In[27]:


df1.to_csv("방문객_통계.csv")

