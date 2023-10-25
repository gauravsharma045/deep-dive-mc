#!/usr/bin/env python
# coding: utf-8

# In[1]:


import json
import pandas as pd
with open("func.json","r") as file:
    data=json.load(file)


# In[2]:


df = pd.json_normalize(data)


# In[3]:


df.columns


# In[4]:


df['order.order_purchase_date'] = pd.to_datetime(df['order.order_purchase_date'])
df['month_name'] = df['order.order_purchase_date'].dt.strftime('%B')
df


# In[5]:


monthly_sales = df.groupby('month_name')['sales_amt'].sum().reset_index()


# In[6]:


highest_sales_month = monthly_sales[monthly_sales['sales_amt'] == monthly_sales['sales_amt'].max()]


# In[18]:


highest_sales_month


# In[27]:


df["profit_amt"] = df["profit_amt"].replace('null', None)


# In[35]:


df['profit_amt'] = df.profit_amt.fillna('')


# In[36]:


monthly_profit=df.groupby('month_name')['profit_amt'].sum().reset_index()


# In[22]:


highest_profit_month = monthly_profit[monthly_profit['profit_amt'] == monthly_profit['profit_amt'].max()]


# In[ ]:




