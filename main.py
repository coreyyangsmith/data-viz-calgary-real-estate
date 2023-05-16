#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thurs May 11

@author: corey
"""

# Corey Yang-Smith
# May 11 2023
# Practicing chloropleth visualization of Calgary data.
# Practicing data cleaning and preparation, and further working with geojson files.
# 
# Dataset
# https://data.calgary.ca/Government/Total-Property-Assessed-Value/dmd8-bmxh
#
#
#
################################################################################################################################

#Import Libraries
import geopandas as gpd
import pandas as pd

import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns

import folium
from folium.features import GeoJsonTooltip


###############################################################################

YEARS = [2005,2006,2007,2008,2009,2010,
         2011,2012,2013,2014,2015,2016,
         2017,2018,2019,2020,2021,2022]

FILE_NAMES = ["year_2005.csv","year_2006.csv","year_2007.csv",
            "year_2008.csv","year_2009.csv","year_2010.csv",
            "year_2011.csv","year_2012.csv","year_2013.csv",
            "year_2014.csv","year_2015.csv","year_2016.csv",
            "year_2017.csv","year_2018.csv","year_2019.csv",
            "year_2020.csv","year_2021.csv","year_2022.csv"]

SECTORS = []

COMM_CODES = ['TAR', 'SIL', 'BOW', 'SAD', 'SRI', 'CIA', 'MRT', 'DBC', 'HUN', 'THO', 'MAL', 'EDG',
 'SNA', 'MCI', 'DAL', 'RAN', 'HAW', 'SCE', 'ARB', 'VAR', 'BRE', 'TEM', 'CHW', 'NHV',
 'NHU', 'GRV', 'SKW', 'CAS', 'SKE', 'WES', 'FAL', 'WHI', 'HIW', 'HOR', 'NAW', 'PEG',
 'GRI', 'WIN', 'HPK', 'QPK', 'CAM', 'RMT', 'COL', 'NPK', 'BNF', 'UOC', '01E', '06B',
 'MON', 'PAT', 'UNI', 'STA', 'CAP', 'TUX', 'RUN', 'MOP', 'REN', 'SAW', 'VIS', 'SUN',
 'PIN', 'MPK', 'FHT', 'PEN', 'MRL', 'MER', 'FRA', 'MLI', 'BRD', 'CRE', 'SSD', 'CHN',
 'EAU', 'RDL', 'HIL', 'WHL', 'HOU', 'PKD', 'SPR', 'WLD', 'POI', 'COA', 'RCK', 'STR',
 'WGT', 'CHR', 'SHG', 'SCA', 'SSW', 'DNW', 'DNC', 'BLN', 'DNE', 'RAM', 'ING', 'ALB',
 'FLN', 'DOV', 'RED', 'FLI', '10B', 'ERI', 'SOV', 'AYB', 'MNI', 'HIF', 'MIS', 'PKH',
 'RID', 'ROX', 'ERL', 'LMR', 'UMR', 'RIC', 'EPK', 'CLI', 'BNK', 'SOC', 'KIL', 'RUT',
 'GDL', 'GBK', 'GLA', 'SIG', 'ALT', 'CFC', 'LPK', 'EYA', 'BRT', 'MAN', '09D', 'VAF',
 'BUR', 'FHI', 'GTI', 'OGD', 'EFI', 'STD', 'OSH', '09H', 'WND', 'GPK', 'MEA', 'BEL',
 'MAF', 'NGM', 'LKV', 'KIN', 'EAG', 'KEL', 'CHK', 'FAI', 'FVI', 'RIV', 'ACA', 'EFV',
 'GBP', 'SFH', 'S23', 'GPI', 'ESH', 'SHI', 'MPL', 'HAY', 'PUM', 'PAL', 'BYV', 'CED',
 'BRA', 'OAK', 'SOW', 'WOO', 'SHS', 'DRN', 'MID', 'WIL', 'DIA', 'DDG', 'FPK', 'QLD',
 'LKB', 'BDO', 'CAN', 'WBN', '13B', 'EVE', 'PKL', 'DRG', 'MCK', 'SDC', 'MLR', 'SHN',
 '13D', '01B', 'TUS', 'VAL', 'GRE', '01D', '01C', 'CGR', 'WSP', 'ASP', 'SPH', 'DIS',
 '06A', 'COP', 'ROY', 'CIT', 'HAM', 'EVN', 'KCA', 'MAC', 'BED', 'SAN', 'ABP', 'MCT',
 'ST4', 'CRA', 'CHA', 'PAN', 'ROC', 'BRI', 'COR', 'HID', '09N', '03I', 'COV', 'SOM',
 'NEB', '02C', 'RYV', 'CPF', '03H', '03D', 'RSN', '12B', '12C', 'CFL', '13G', 'CHV',
 'ST2', 'ABB', 'AUB', 'MOR', 'ST1', 'SVO', 'CRM', 'SHW', 'APP', '02F', 'SET', 'COU',
 '03C', '02A', '09K', 'LEG', '14U', '14V', '12A', '01F', 'HAR', 'SGL', '12F', '05B']

SELECTED_COMM_CODE = "COU"

SELECTED_YEAR = 2022

###############################################################################

# Data Importing
community_center = "community_center.csv"
comm_center = pd.read_csv(community_center)

# Geo Pandas Dataset Setup
imported_file = str(SELECTED_YEAR) + "/" + SELECTED_COMM_CODE + ".csv"

geo_import = gpd.read_file(imported_file)
geo_import['MULTIPOLYGON'] = gpd.GeoSeries.from_wkt(geo_import['MULTIPOLYGON'])
geo_import['geometry'] = geo_import['MULTIPOLYGON']
geo_import = geo_import[['COMM_CODE', 'geometry', 'ADDRESS', 'ASSESSED_VALUE', 'COMM_NAME']]
# geo_import = geo_import.dropna(axis=0) #drop na

geo_import.astype({'ASSESSED_VALUE': 'float32'}) # change type 

geojson=geo_import
geojson = geojson.set_crs("EPSG:4326")

geojson = pd.merge(left = geojson,
                   right = comm_center,
                   left_on = "COMM_NAME",
                   right_on = "Community Name",
                   how = 'left')
print("\nMerge Commplete")

###############################################################################

# Map Initialization
##TODO, select based on location NW NE SW SE
#TODO Automatically select location based on centre of neighbourhood lat/long



m = folium.Map(location=[51.0447, -114.0719], 
               zoom_start=10,
               tiles="OpenStreetMap",
               zoom_control=False) # Calgary

df = pd.read_csv(imported_file)
                 
                 
# Formatting Float to Dollars
# df['ASSESSED_VALUE'] = '${:,.2f}'.format(df['ASSESSED_VALUE'].astype(float))
dollars = df['ASSESSED_VALUE'].apply(lambda x: "${:,.0f}".format((x)))
geojson['DOLLARS'] = dollars

print (geojson.dtypes)

#TODO get centre of locations
# Folium Map Information
m = folium.Map(location=[51.0447, -114.0719], 
               zoom_start=10,
               tiles="OpenStreetMap",
               zoom_control=False) # Calgary


# =============================================================================
# # Continuous Legend
# import branca.colormap as cmp
# linear = cmp.LinearColormap(
#     ['red', 'yellow', 'green'],
#     vmin=0, vmax=1000000,
#     caption='Color Scale for Map' #Caption for Color scale or Legend
# )
# 
# folium.GeoJson(
#     geojson,
#     style_function=lambda feature: {
#         'fillColor' : linear(ecuador_dict[feature["ASSESSED_VALUE"]]),
#         'color': 'black',     #border color for the color fills
#         'weight': 1,          #how thick the border has to be
#         'dashArray': '5, 10'  #dashed lines length,space between them
#     }
# ).add_to(m)
# linear.add_to(m)   #adds colorscale or legend
#  #         'fillColor': linear(geojson[feature["id"]]), cannot get this line to work
# =============================================================================

cp = folium.Choropleth(geo_data = geojson,
                       name='2022',
                       data = df,
                       columns = ["COMM_CODE", "ASSESSED_VALUE"],
                       key_on = 'feature.properties.COMM_CODE',
                       fill_color = 'BuPu',
                       nan_fill_color="White", #Use white color if there is no data available for the county
                       fill_opacity=0.7,
                       line_opacity=0.2,
                       legend_name='Property Value in 2022', #title of the legend
                       highlight=True,
                       line_color='black').add_to(m)

fields = ["ADDRESS", "DOLLARS", "COMM_CODE", "COMM_NAME"]
aliases = ["Address:", "Assessed Value:", "Community Code:", "Community Name:"]

folium.GeoJsonTooltip(fields = fields,
                      aliases = aliases,
                      labels=True,
                      localize=True,
                      style = ("background-color: #F0EFEF; border: 2px solid black; border-radius: 3px; box-shader: 3px")).add_to(cp.geojson)


print("")
print("Tooltips successfully added.")

folium.LayerControl().add_to(m)

m.save("myMap.html")

print("")
print("")
print("###########################")
print("Code Successfully Executed!")
print("###########################")