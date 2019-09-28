# Databricks notebook source
from sklearn.datasets import load_iris
import pandas as pd

# COMMAND ----------

data=load_iris()
df=pd.DataFrame(data["data"])
df["target"]=data["target"]
df.head()

# COMMAND ----------

# MAGIC %fs 
# MAGIC ls

# COMMAND ----------

df["target"].value_counts()

# COMMAND ----------

from sklearn.neighbors import  KNeighborsClassifier
clf=KNeighborsClassifier(n_neighbors=3)

# COMMAND ----------

clf.fit(df.loc[:,[0,1,2,3]].values,df["target"].values)

# COMMAND ----------

import pickle

# COMMAND ----------

filename = '/dbfs/FileStore/tables/finalized_modelpy.pickle'
pickle.dump(clf, open(filename, 'wb'))

# COMMAND ----------

clf.predict(df.loc[:,[0,1,2,3]])

# COMMAND ----------

df.info()

# COMMAND ----------

df.loc[0,[0,1,2,3]].astype(str).to_dict()

# COMMAND ----------


