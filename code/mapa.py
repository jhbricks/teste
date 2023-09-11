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

#https://discuss.streamlit.io/t/how-to-build-an-unique-button-in-streamlit-web-program/12012/28?page=2

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #ce1126;
    color: white;
    height: 3em;
    width: 12em;
    border-radius:10px;
    border:3px solid #ce1126;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
}

div.stButton > button:hover {
	background:linear-gradient(to bottom, #ce1126 5%, #ff5a5a 100%);
	background-color:#ce1126;
}

div.stButton > button:active {
	position:relative;
	top:3px;
}

</style>""", unsafe_allow_html=True)

b = st.button("Button 1")


st.markdown('<p></p>', unsafe_allow_html = True)
st.markdown('<p></p>', unsafe_allow_html = True)
st.markdown('<p></p>', unsafe_allow_html = True)

c = st.button("Button 2")

m = st.markdown("""
<style>
div.stButton > button:first-child {
    background-color: #000000;
    color: white;
    height: 3em;
    width: 12em;
    border-radius:10px;
    border:3px solid #ce1126;
    font-size:20px;
    font-weight: bold;
    margin: auto;
    display: block;
}

div.stButton > button:hover {
	background:linear-gradient(to bottom, #ce1126 5%, #ff5a5a 100%);
	background-color:#ce1126;
}

div.stButton > button:active {
	position:relative;
	top:3px;
}

</style>""", unsafe_allow_html=True)

d = st.button("teste")