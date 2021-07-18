
import pandas as pd
import streamlit as st

import sys, os
sys.path.append(os.path.abspath(os.path.join('..')))

@st.cache(allow_output_mutation=True)
def loadData1():
    df=pd.read_csv('data/cleaned_modified_data.csv')
    return df


@st.cache
def loadData2():
    df_scored=pd.read_csv('data/satisfaction_score.csv')
    return df_scored