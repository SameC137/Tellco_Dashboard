
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

sys.path.insert(0, '../scripts')

import streamlit as st
import pandas as pd
import numpy as np



from telldashboard.scripts.scripts import *
from telldashboard.scripts.data_loaders import loadData1

def app():
    st.title("Session Data")
    df=loadData1().copy()
    
    num=st.slider("Select number of values", 10, 1000, 5,key=3)
    # group= st.selectbox('GroupBy',["None",list(df.columns[1:])])

    sorted=df[['Handset Type','MSISDN/Number']].groupby(['Handset Type'])['MSISDN/Number'] \
                             .nunique() \
                             .reset_index(name='Number of Devices') \
                             .sort_values(['Number of Devices'], ascending=False) \
                             .head(num)

    st.write(sorted)


    f={
        
        'MSISDN/Number': 'count',
        'Bearer Id': 'count',
        'Dur. (ms)':'sum',
        'Social Media DL (Bytes)' : 'sum',
        'Social Media UL (Bytes)' : 'sum',
        'Google DL (Bytes)' : 'sum', 
        'Google UL (Bytes)' : 'sum',
        'Email DL (Bytes)' : 'sum', 
        'Email UL (Bytes)' : 'sum',
        'Youtube DL (Bytes)' : 'sum', 
        'Youtube UL (Bytes)' : 'sum',
        'Netflix DL (Bytes)' : 'sum', 
        'Netflix UL (Bytes)' : 'sum',
        'Gaming DL (Bytes)' : 'sum', 
        'Gaming UL (Bytes)' : 'sum',
        'Other DL (Bytes)' : 'sum', 
        'Other UL (Bytes)' : 'sum',
        'Total DL (Bytes)' : 'sum', 
        'Total UL (Bytes)' : 'sum',
    }


    dfAgg=df.groupby(['Handset Type']).agg(f)
    dfAgg=dfAgg.rename(columns={'MSISDN/Number':'Number of Users','Bearer Id':"Number of Sessions"})
    
    selec= st.selectbox('Selection',["None","Top","Bottom"])   
    column=st.selectbox('Column',dfAgg.columns)
    num=st.slider("Select number of values", 10, 1000, 5,key=2)
    if selec=="Top":
        writeDf=getTop(dfAgg,column,num)
    elif selec=="None":
        writeDf=dfAgg.head(num)
    else:
        writeDf=getBottom(dfAgg,column,num)
    st.write(writeDf)