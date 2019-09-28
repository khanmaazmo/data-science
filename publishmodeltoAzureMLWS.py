# Databricks notebook source
from azureml import Workspace

# COMMAND ----------

import pickle
import numpy as np
import pandas as pd

# COMMAND ----------

from sklearn.neighbors import  KNeighborsClassifier

# COMMAND ----------

#load machine learning model here into a model variable
filename="finalized_modelpy.pickle"
filepath="/dbfs/FileStore/tables/"
clf=pickle.load(open(filepath+filename, 'rb'))

# COMMAND ----------

#mlws_workspaceid 987a9f66-97a0-4c90-b624-4e18ba7b7c12
#mlws_authorizationkey ---get it from somewhere
#ws = Workspace()
#one more place i saw below single line code to define workspace


# COMMAND ----------

workspace_id = ws.workspace_id
authorization_token = ws.authorization_token
print(workspace_id)
print(authorization_token)

# COMMAND ----------

from azureml import services

# COMMAND ----------

# set up web service
workspace_id = '9fe8f2f9e9f94677abc6d076340fcbf7'
authorization_token = 'ghRbG40tVVy8IUGRYaPAo7cam6Nkv6Bn9qha4guFm0rhaiPHFGOaBD3xajad8o+h+baNRCFXaXT5qz9M1VpbGg=='
ws = Workspace (workspace_id='fa817a79ba3b4cac86eb053ed001a566',authorization_token='/KQWsvqg0dtfp3vOjiazPEWABxFni41TXHjYcvRMhqRquP2hqO36uZ4Q/tqHaq+G7nMDJB668hmOvMle4lm/Ew==',endpoint='https://studioapi.azureml-int.net')
from azureml import services
@services.publish(workspace_id, authorization_token)
@services.types(a=float, b=float, c=float, d=float)
@services.returns(float)
def demoservice(a,b,c,d):
    # predict the label
    feature_vector = [a,b,c,d]
    return clf.predict(feature_vector)


# COMMAND ----------


# save information about the web service
service_url = demoservice.service.url 
api_key = demoservice.service.api_key
help_url = demoservice.service.help_url
service_id = demoservice.service.service_id
print(service_url)
print(api_key)
print(help_url)
print(service_id)
