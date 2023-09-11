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

if st.button('Button 1'):
    st.write('Button 1 was clicked')
    if st.button('Button 2'):
        # This will never be executed.
        st.write('Button 2 was clicked')
