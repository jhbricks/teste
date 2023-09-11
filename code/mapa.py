import streamlit as st
import geopandas as gpd
import leafmap
import pandas as pd
import numpy as np
import folium
import leafmap.foliumap as leafmap
import geopandas
import mapclassify
import matplotlib.pyplot as plt

import streamlit as st

import streamlit as st
st.markdown(""" div.stButton > button:first-child {
background-color: #00cc00;color:white;font-size:20px;height:3em;width:50%;border-radius:10px 10px 10px 10px;
}
“”", unsafe_allow_html=True)

col1,col2,col3=st.beta_columns([0.3,1.2,0.3])
with col1:
    st.empty()
with col2:
    if st.button(“the notice you want to show”):
        st.write(“content you want to show”)
with col3:
    st.empty()
