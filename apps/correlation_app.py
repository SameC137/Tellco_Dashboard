
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
sys.path.insert(0, '../scripts')

import streamlit as st
import numpy as np
import pandas as pd

import seaborn as sns
import matplotlib.pyplot as plt


from apps.scripts import *
from apps.data_loaders import loadData1

def app():
    st.title("Correlation ")
    
    st.markdown("Correlation between the different aggregated columns by users")

    df=loadData1().copy()
    df=form_combination_columns(df)
    f={     'Bearer Id': 'count',
        'Dur. (ms)':'sum',
        'Social Media (Bytes)' : 'sum',
        'Google (Bytes)' : 'sum', 
        'Email (Bytes)' : 'sum', 
        'Youtube (Bytes)' : 'sum', 
        'Netflix (Bytes)' : 'sum', 
        'Gaming (Bytes)' : 'sum', 
        'Other (Bytes)' : 'sum', 
        'Total Data (Bytes)' : 'sum', 
    }


    dfAgg=df.groupby(['MSISDN/Number']).agg(f)

    fig4=plt.figure(figsize=(30, 16))    
    sns.heatmap(dfAgg.corr(method='pearson'), cmap="YlGnBu", annot=True,linewidths=.5)
    st.pyplot(fig4)
