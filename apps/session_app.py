
import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

sys.path.insert(0, '../scripts')

import streamlit as st
import pandas as pd
import numpy as np

from apps.scripts import *
from apps.data_loaders import loadData1

def app():
    st.title("Session Data")
    df=loadData1().copy()
    column=st.selectbox('Column',df.columns[1:])
    # group= st.selectbox('GroupBy',["None",list(df.columns[1:])])

    selec= st.selectbox('Selection',["None","Top","Most Frequent","Bottom"])
    num=st.slider("Select number of values", 10, 1000, 5)
    if selec=="Top":
        writeDf=getTop(df,column,num)
    elif selec=="Most Frequent":
        writeDf=getMostFrequent(df,column,num)
    elif selec=="None":
        writeDf=df.head(num)
    else:
        writeDf=getBottom(df,column,num)

    st.write(writeDf)


