
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))
sys.path.insert(0, '../scripts')

import streamlit as st
import numpy as np
import pandas as pd


from apps.scripts import *
from apps.data_loaders import loadData2

def app():
    
    
    st.title("User Satisfaction Data ")
    st.subheader("with Experience, Satisfaction and Engagement Scores")
    df_scored=loadData2().copy()
    selec= st.selectbox('Selection',["None","Top","Bottom"])   
    column=st.selectbox('Column',df_scored.columns[1:])
    num=st.slider("Select number of values", 10, 1000, 5,key=2)
    if selec=="Top":
        writeDf=getTop(df_scored,column,num)
    elif selec=="None":
        writeDf=df_scored.head(num)
    else:
        writeDf=getBottom(df_scored,column,num)

    st.write(writeDf)
