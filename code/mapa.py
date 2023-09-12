import streamlit as st
import geopandas as gpd
import leafmap
import pandas as pd
import numpy as np
import folium
import leafmap.foliumap as leafmap
#import libpysal
import geopandas
import mapclassify
import matplotlib.pyplot as plt
import streamlit.components.v1 

########################ARQUIVOS CSV E GEOJSON
contexto = "./dados/csv/contexto.csv"
pop = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/pop_2021.csv"
renda = "./dados/csv/renda.csv"
riqueza = "./dados/csv/riqueza.csv"
PR = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson"
NTC =  "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson"

area = 'PR'
arq = pop
ind = 'População'
scheme = 'FisherJenks'
k = 7 
cmap = 'Reds' 
fields = ['Município','População'] 
title = 'teste'





######encaminha o geojson da area
#if area == 'PR':
#    arq_g = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson"
#else:
#    area = 'NTC'
#    arq_g = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson"

#######MERGE geojson e csv
arq_csv = pd.read_csv("https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/pop_2021.csv")
arq_geojson = gpd.read_file('https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson')
data = arq_geojson.merge(arq_csv, on="Município")

#######LAT E LON CENTRAIS

    
if not isinstance(data,gpd.GeoDataFrame):
    print("O arquivo não é um GeoDataFrame")
    exit()


m = leafmap.Map(width=900, height=600,
                draw_control=False,
                measure_control=False,
                fullscreen_control=False,
                attribution_control=True)

#style = {"stroke": True,"color": "#000000","weight": 2,"opacity": 1}
hover_style = {"fillOpacity": 0.7}

m.add_data(data,column='População',scheme='FisherJenks',k=7,cmap='Reds',fields=['Município','População'],
            zoom_to_layer=True,
            style_fuction={"stroke": True,"color": "#000000","weight": 2,"opacity": 1},
            hover_style=hover_style)
 
m.to_streamlit()
        # ZOOM 
#if area == PR:
#    m.zoom_to_bounds((-26.80, -54.67, -22.44, -47.98))
#else:
#    m.zoom_to_bounds((-25.85,-48.54,-24.96, -47.87))
#D - EAST
#N 
#E - WEST
#S
#EAST    NORTH    WEST    SOUTH
#(-47.98, -22.44, -54.67, -26.80)         #PR
#(-47.87,-24.96,-48.54, -25.85)             #NTC
  #  [[south, west], [north, east]].
    #self.fit_bounds([[bounds[1], bounds[0]], [bounds[3], bounds[2]]])


