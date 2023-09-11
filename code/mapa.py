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


@st.cache_data

def mapagvf(area, arq, ind, scheme, k, cmap, fields, title):
######encaminha o geojson da area
    if area == 'PR':
        arq_g = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson"
    else:
        area = 'NTC'
        arq_g = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson"

#######MERGE geojson e csv
    arq_csv = pd.read_csv(arq)
    arq_geojson = gpd.read_file(arq_g)
    data = arq_geojson.merge(arq_csv, on="Município")

#######LAT E LON CENTRAIS
    ponto_central = arq_geojson.geometry.centroid
    lat = ponto_central.iloc[0].y
    lon = ponto_central.iloc[0].x
    
    if not isinstance(data,gpd.GeoDataFrame):
        print("O arquivo não é um GeoDataFrame")
        exit()

#Lat e Lon Centrais
    ponto_central = data.geometry.centroid
    lat = ponto_central.iloc[0].y
    lon = ponto_central.iloc[0].x

    m = leafmap.Map(width=900, height=600, center=[lat, lon],
                    draw_control=False,
                    measure_control=False,
                    fullscreen_control=False,
                    attribution_control=True)

        # ZOOM 
    if area == PR:
        m.zoom_to_bounds((-26.80, -54.67, -22.44, -47.98))
    else:
        m.zoom_to_bounds((-25.85,-48.54,-24.96, -47.87))
#D - EAST
#N 
#E - WEST
#S
#EAST    NORTH    WEST    SOUTH
#(-47.98, -22.44, -54.67, -26.80)         #PR
#(-47.87,-24.96,-48.54, -25.85)             #NTC
  #  [[south, west], [north, east]].
    #self.fit_bounds([[bounds[1], bounds[0]], [bounds[3], bounds[2]]])
    m.add_data(data=data,
               column=ind,
               scheme=scheme,
               k=k,
               cmap=cmap,
               fields=fields,
               legend_title=title,
               legend_position='Bottomright',
               layer_name=title,
               )

        ########VALORES DE MX E MN DAS VARIAVEIS
    max_value = data[ind].max()
    min_value = data[ind].min()
    max_municipio = data.loc[data[ind] == max_value, "Município"].iloc[0]
    min_municipio = data.loc[data[ind] == min_value, "Município"].iloc[0]

        #####ADICIONAR MX E MN NO MAPA
    folium.Marker([data.loc[data[ind] == max_value, "Y"].iloc[0],
                   data.loc[data[ind] == max_value, "X"].iloc[0]],
                   popup=f"Maior valor: {max_value}<br>{max_municipio}",
                   icon=folium.Icon(color="darkpurple", icon="arrow-up"),
                   ).add_to(m)
    folium.Marker([data.loc[data[ind] == min_value, "Y"].iloc[0],
                   data.loc[data[ind] == min_value, "X"].iloc[0]],
                   popup=f"Menor valor: {min_value}<br>{min_municipio}",
                   icon=folium.Icon(color="purple", icon="arrow-down"),
                   ).add_to(m)
    
    m.to_streamlit

