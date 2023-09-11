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






import streamlit as st
import streamlit.components.v1 as components

def ChangeButtonStyle(widget_label, background_color, style):
    htmlstr = f"""
        <script>
            var elements = window.parent.document.querySelectorAll('button');
            for (var i = 0; i < elements.length; ++i) {{ 
                if (elements[i].innerText == '{widget_label}') {{ 
                    elements[i].style.background = '{background_color}'; {{
                    {style}
                    }}
                }}
            }}
        </script>
        """
    components.html(f"{htmlstr}", height=0, width=0)

# Define the style you want to apply to all buttons
global_button_style = """
    elements[i].style.color = 'white';
    elements[i].style.height = '3em';
    elements[i].style.width = '12em';
    elements[i].style.borderRadius = '10px';
    elements[i].style.fontSize = '20px';
    elements[i].style.fontWeight = 'bold';
    elements[i].style.margin = 'auto';
    elements[i].style.display = 'block';
    
"""

# Create the buttons
cols = st.columns(2)

cols[0].button('second button', key='b2')
cols[1].button('fourth button', key='b4')

# Apply the global style to all buttons (This will apply the style to all buttons initially)
ChangeButtonStyle('second button', '#ce1126', global_button_style)
ChangeButtonStyle('fourth button', '#354b75', global_button_style)
