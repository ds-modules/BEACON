#!/usr/bin/env python
# coding: utf-8
# %%

# %%


#Import statements
import os
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from numpy import NaN
from decimal import Decimal
import pandas as pd
import math
import datetime
from datetime import time
import calendar
import seaborn as sns
from IPython.core.display import display, HTML
import itertools
import scipy
display(HTML("<style>.container { width:100% !important; }</style>"))


# %%


#This function will pull in the BEACO2N CO2 data from all the node IDs listed for the given start date and end date
def co2(start,end,*nodes):
    full = pd.DataFrame()
    for node in nodes:
        print(node)
        parameter = 'co2_corrected_avg_t_drift_applied-level-2'
        filename="http://128.32.208.8/node/"+node+"/measurements_all/csv?name=Supersite&interval=60&variables="+parameter+"&start="+start+"&end="+end
        data  = pd.read_csv(filename, on_bad_lines="skip",index_col=[0], parse_dates=[0]) 
        data = data.rename(columns={parameter:node})
        data = data.drop(['epoch','node_id','node_file_id','datetime'],axis = 1)
        data.replace(-999, np.nan, inplace=True)
        data.replace(-111, np.nan, inplace=True)
        full = pd.merge(full,data, how = 'outer',left_index=True,right_index=True) 
    return full


# %%


#Pulling the data - you can change the start and end date, as well as the node IDs
co2_bay1 = co2('2020-09-15%2000:00:00','2020-10-27%2000:00:00','4','13','14','15','17','20','21','22','25','26','28')
co2_bay2 = co2('2020-09-15%2000:00:00','2020-10-27%2000:00:00','31','33','37','38','41','42','43','45','48','54')
co2_bay3 = co2('2020-09-15%2000:00:00','2020-10-27%2000:00:00','58','59','60','62','63')


# %%

#Creating a dataframe of CO2 concentrations. The columns are the node IDs
co2_bay = pd.concat([co2_bay1, co2_bay2, co2_bay3], axis = 1)
co2_bay


# %%


#Pulling the lat/long for each node for mapping
nodes = pd.read_csv("get_latest_nodes.csv")
nodes = nodes.drop(columns=['node_name','node_name_long','node_folder_id','height_above_ground','height_above_sea','deployed','datetime','PM_ug/m3','PM_ug/m3_QC_level','co_ppm','co_ppm_QC_level','co2_ppm','co2_ppm_QC_level','groups'])
nodes = nodes.set_index('id')
nodes


# %%


## Filtering to just the sites we used
nodes_list = (4,13,14,15,17,20,21,22,25,26,28,31,33,37,38,41,42,43,45,48,54,58,59,60,62,63)


# %%


nodes = nodes[nodes.index.isin(nodes_list)]
nodes


# %%





# %%
