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

########################ARQUIVOS CSV E GEOJSON
#contexto = "./dados/csv/contexto.csv"
pop = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/pop_2021.csv"
#renda = "./dados/csv/renda.csv"
#riqueza = "./dados/csv/riqueza.csv"
PR = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson"
NTC =  "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson"


######encaminha o geojson da area
#    if area == 'PR':
#        arq_g = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson"
 #   else:
  #      area = 'NTC'
   #     arq_g = "https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/NTC.geojson"

#######MERGE geojson e csv
    
arq_csv = pd.read_csv("https://raw.githubusercontent.com/jhbricks/mapades/main/dados/csv/pop_2021.csv")
arq_geojson = gpd.read_file("https://raw.githubusercontent.com/jhbricks/mapades/main/dados/geojson/PR.geojson")
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
#if area == PR:
m.zoom_to_bounds((-47.98, -22.44, -54.67, -26.80))
# else:
#        m.zoom_to_bounds((-47.87,-24.96,-48.54, -25.85))

style_style = {"stroke": True,           #linha da borda vai ser desenhada
               "color": "#000000",       #cor da linha (preto)
               "weight": 2,              #espessura 2 px
               #"opacity": 0,             #opacidade da borda (1 = totalmente opaca)
               "fillOpacity": 1,       #opacidade do preenchimento (0.1 = 10% opaca)
               "clickable": True,
               }
m.add_data(data=data,
           column='População',
           scheme='FisherJenks',
           k=7,
           cmap='YlOrBr',
           fields=['Município','População'],
           legend_title='População residente',
           legend_position='Bottomright',
           layer_name='title',
           style = style_style,
           )
ind = 'População'
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
