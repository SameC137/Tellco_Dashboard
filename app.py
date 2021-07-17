import numpy as np
import pandas as pd
import streamlit as st
# import plotly.express as px
# from scripts.scripts import *
from multiapp import MultiApp 

from apps import experience_app, session_app, handset_app



st.set_page_config(page_title="Tellco Analysis", layout="wide")



app = MultiApp()

# Add all your application here
app.add_app("Satisfaction Data View", experience_app.app)
app.add_app("Session Data View", session_app.app)

app.add_app("Handet Data View", handset_app.app)

# The main app
app.run()
