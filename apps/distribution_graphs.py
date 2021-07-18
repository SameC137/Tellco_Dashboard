

    
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
    st.title("Distribution Graphs ")
    

    df=loadData1().copy()
    
    df=form_combination_columns(df)
    # print(df["Total Data (Bytes)"].head(5))
    
    column=st.selectbox('Column',["Social Media (Bytes)", "Youtube (Bytes)","Netflix (Bytes)", "Google (Bytes)", \
         "Email (Bytes)", "Gaming (Bytes)", "Other (Bytes)" ,  "Total Data (Bytes)"])


    fig4=plt.figure(figsize=(30, 16))    
    sns.histplot(data=df[column], color='red', kde=True)
    # plt.title(f'Distribution of {column}', size=20, fontweight='bold')
    st.pyplot(fig4)
