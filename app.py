import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
from Scripts.scripts import *

st.set_page_config(page_title="Tellco Analysis", layout="wide")

dataframe=''
def prepareData():
    st.title("Tweet Text Word Cloud")
    df=pd.read_csv('./Data/cleaned_modified_data.csv')
    column=st.selectbox('Column',df.columns[1:])
    
    # group= st.selectbox('GroupBy',["None",list(df.columns[1:])])

    selec= st.selectbox('Selection',["None","Top","Most Frequent","Bottom"])
    num=st.slider("Select number of values", 10, 50, 5)
    if selec=="Top":
        writeDf=getTop(df,column,num)
    elif selec=="Most Frequent":
        writeDf=getMostFrequent(df,column,num)
    elif selec=="None":
        writeDf=df.head(num)
    else:
        writeDf=getBottom(df,column,num)

    st.write(writeDf)

def prepareData2():
    
    st.title("Tweet Text Word Cloud")
    df_scored=pd.read_csv('./Data/satisfaction_score.csv')
    selec= st.selectbox('Selection',["Top","Bottom"])   
    column=st.selectbox('Column',df_scored.columns[1:])
    num=st.slider("Select number of values", 10, 50, 5,key=2)
    if selec=="Top":
        writeDf=getTop(df_scored,column,num)
    else:
        writeDf=getBottom(df_scored,column,num)

    st.write(writeDf)
prepareData()
prepareData2()

# def selectData():
