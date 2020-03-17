
# coding: utf-8

# # 本金平均攤還 

# ## 輸入資料：本金、年期數、年利率

# In[1]:


principle = int(input("Input the value of principle:(請輸入本金金額)："))  #本金


# In[2]:


year = float(input("Input the year of loan period:(請輸入貸款年期)："))  #年期數


# In[3]:


rate = float(input("Input the annual interest rate(%):(請輸入年利率(%))："))  #年利率


# ## 計算每月(期)需還之本金、利息及本金利息累計

# In[4]:


#四捨五入到整數第一位的函數
def rnd(x):
    if x*10-int(x)*10 <5:
        return int(x)
    else:
        return int(x)+1


# In[5]:


from math import ceil
avg_prin_per_mon = ceil(principle/int(year*12))  #計算每月平均需還本金(採無條件進入法)
mon_rate = rate/12
prin_mon_pay = []  #每月需還本金串列
inte_mon_pay = []  #每月需還利息串列
all_accu_pay = []  #每月本金利息累計

for i in range(int(year*12)):
    prin_mon_pay.append(min(avg_prin_per_mon,principle-avg_prin_per_mon*i))  #最末月需調整金額
    inte_mon_pay.append(rnd((principle-avg_prin_per_mon*i)*mon_rate/100))  #利息採四捨五入法
    all_accu_pay.append(sum(prin_mon_pay) + sum(inte_mon_pay))


# ## 輸出：每月攤還本金,利息及本利累積之一覽表

# In[6]:

import os
import pandas as pd 
data = {'本金(元)':prin_mon_pay, '利息(元)':inte_mon_pay, '本利累計(元)':all_accu_pay}
col_names = []
for i in range(int(year*12)):
    col_names.append("第"+str(i+1)+"期")
df = pd.DataFrame(data,index=col_names)
df
print(df)

os.system("pause")
