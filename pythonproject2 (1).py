#!/usr/bin/env python
# coding: utf-8

# # Proje 2
# 
# ## (Dataset Linki: https://www.kaggle.com/datasets/luiscorter/netflix-original-films-imdb-scores )
# 
# 
# 
# 
# * 1.Veri setine göre uzun soluklu filmler hangi dilde oluşturulmuştur? Görselleştirme yapınız.
# * 2.2019 Ocak ile 2020 Haziran tarihleri arasında 'Documentary' türünde çekilmiş filmlerin IMDB değerlerini bulup görselleştiriniz.
# * ++++3.İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?
# * ++++4.'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?
# * 5.'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.
# * 6.++++Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.
# * 7.+++++IMDB puanı en yüksek olan ilk 10 film hangileridir?
# * 8.++++++++++IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.
# * +++++++++9.IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.
# * +++++10.'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.
# * 11.++++++Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz.
# * ++++12.Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz.
# * 13.++++++++Hangi yılın toplam "runtime" süresi en fazladır?
# * 14.Her bir dilin en fazla kullanıldığı "Genre" nedir?
# * 15.Veri setinde outlier veri var mıdır? Açıklayınız.
# 
# 

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data_= pd.read_csv(r"C:\Users\90538\Desktop\global_AI_hub\archive\NetflixOriginals.csv",encoding='latin-1')


# In[3]:


df=pd.DataFrame(data_)


# In[38]:


df=df.copy()


# In[ ]:


df.head()


# In[ ]:


df.dtypes


# In[ ]:


df.isnull().any()


# In[ ]:


df.describe()


# # 13.+++++Hangi yılın toplam "runtime" süresi en fazladır?

# In[31]:


df["Premiere"]=df["Premiere"].str.replace("," , " ")
df["Premiere"]=df["Premiere"].str.replace(" " , "-")
df["Premiere"]=df["Premiere"].str.replace("--" , "-")
pd_serisi= list(df["Premiere"])
yıl=[]
for i in range(0,584):
    yıl.append(pd_serisi[i][-4:])


# In[36]:


df["Yıl"] = yıl
df["Adet"]=1
yillara_gore_grupladik=df.groupby(df["Yıl"]).sum()
en_cok_runtime=yillara_gore_grupladik.reset_index().sort_values(by="Runtime", ascending=False)


# In[37]:


en_cok_runtime


# ## 11.+++Hangi yılda en fazla film yayımlanmıştır? Görselleştiriniz.

# In[4]:


df["Premiere"]=df["Premiere"].str.replace("," , " ")
df["Premiere"]=df["Premiere"].str.replace(" " , "-")
df["Premiere"]=df["Premiere"].str.replace("--" , "-")
pd_serisi= list(df["Premiere"])


# In[8]:


yıl=[]
for i in range(0,584):
    yıl.append(pd_serisi[i][-4:])


# In[20]:


df["Yıl"] = yıl
df["Adet"]=1
yillara_gore_grupladik=df.groupby(df["Yıl"]).sum()
en_cok_film=yillara_gore_grupladik.reset_index().sort_values(by="Adet", ascending=False)


# In[30]:


en_cok_film


# ## +++++++++8.IMDB puanı ile 'Runtime' arasında nasıl bir korelasyon vardır? İnceleyip görselleştiriniz.

# In[ ]:


df.plot.scatter("IMDB Score","Runtime");


# In[ ]:


#korelasyon yok gibi gözüküyor ama yine de bakıyoruz.


# In[ ]:


df.corr()


# In[ ]:


df["IMDB Score"].corr(df["Runtime"])


# In[ ]:


df["Runtime"].corr(df["IMDB Score"])


# In[ ]:


# düşük negatif korelasyon var.


# In[ ]:


sns.pairplot(df);


# In[ ]:


import seaborn as sns


# In[ ]:


df.head(3)


# In[ ]:


df_heatmap = df.corr()
sns.heatmap(df_heatmap, annot=True)


# ## 9.+++++ IMDB Puanı en yüksek olan ilk 10 'Genre' hangileridir? Görselleştiriniz.

# In[ ]:


df.head()


# In[ ]:


en_yuksek_10_IMDB=df.sort_values(by="IMDB Score", ascending=False).head(10)


# In[ ]:


sns.scatterplot(x="IMDB Score", y="Genre", data= en_yuksek_10_IMDB);


# In[ ]:


sns.barplot(x="IMDB Score", y="Genre", data= en_yuksek_10_IMDB);


# ## 5.'Genre' Sütunu kaç kategoriye sahiptir ve bu kategoriler nelerdir? Görselleştirerek ifade ediniz.

# In[ ]:


df.head(2)


# In[ ]:


yeni_df= df.groupby(df["Genre"]).sum()


# In[ ]:


new_df=yeni_df.reset_index()


# In[ ]:


new_df


# In[ ]:


new_df["Genre"].nunique()


# In[ ]:


Genre= new_df["Genre"]


# In[ ]:


adet= new_df["Adet"]


# In[ ]:


sns.scatterplot(x="Adet" , y="Genre", data= new_df);


# # +++12.Hangi dilde yayımlanan filmler en düşük ortalama IMBD puanına sahiptir? Görselleştiriniz

# In[ ]:


df.head(2)


# In[ ]:


imdb_siralama_kb= df.sort_values("IMDB Score", ascending= True)


# In[ ]:


en_düsük_imdb_hangi_dil= imdb_siralama_kb[0:20]


# In[ ]:


sns.barplot(x="IMDB Score", y= "Language", data=en_düsük_imdb_hangi_dil);


# # 10.++++'Runtime' değeri en yüksek olan ilk 10 film hangileridir? Görselleştiriniz.

# In[ ]:


runtime_siralama=df.sort_values("Runtime", ascending= False)


# In[ ]:


runtime_siralama_ilk_10 =  runtime_siralama[0:10]


# In[ ]:


sns.barplot(x="Runtime", y= "Title", data=runtime_siralama_ilk_10);


# # 7.+++IMDB puanı en yüksek olan ilk 10 film hangileridir?

# In[ ]:


df.head()


# In[ ]:


imdb_siralama= df.sort_values("IMDB Score", ascending= False)


# In[ ]:


en_yuksek_IMDB_10_film=imdb_siralama[0:10]


# In[ ]:


en_yuksek_IMDB_10_film["Title"]


# # 6.+++Veri setinde bulunan filmlerde en çok kullanılan 3 dili bulunuz.

# In[ ]:


df["Adet"]= 1


# In[ ]:


df.head()


# In[ ]:


dilleri_grupladik= df.groupby(df["Language"]).sum()
dilleri_grupladik=dilleri_grupladik.reset_index()
sıraladık=dilleri_grupladik.sort_values(by= "Adet",ascending=False)


# In[ ]:


ımdb_en_yuksek_3= sıraladık[0:3]


# In[ ]:


ımdb_en_yuksek_3


# ## 4. +++'Hindi' Dilinde çekilmiş olan filmlerin ortalama 'runtime' suresi nedir?

# In[ ]:


df.head()


# In[ ]:


hindi_dili= df[df["Language"] == "Hindi"]


# In[ ]:


hindi_dili["Runtime"].mean()


# # 3. +++İngilizce çekilen filmler içerisinde hangi tür en yüksek IMDB puanına sahiptir?

# In[ ]:


eng_films= df[df["Language"] == "English"]
eng_films["IMDB Score"].max()
max_IMDB= eng_films[eng_films["IMDB Score"]==9]
max_IMDB_tur= max_IMDB["Genre"]


# In[ ]:


max_IMDB_tur

