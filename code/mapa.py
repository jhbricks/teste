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

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")

with st.sidebar:
    st.button("button sidebar 1")
    st.button("button sidebar longer text")
    st.button("button sidebar 2")
    st.button("button sidebar 3")

st.button("button page 1")
st.button("button longer text page")
st.button("button page 2")
st.button("button page 3")
external css:

section[data-testid="stSidebar"] div.stButton button {
    background-color: brown;
    width: 200px;
}
