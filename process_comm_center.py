#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 17:14:00 2023

@author: corey
"""

# create community center point
import pandas as pd

imported_file = "calgary_crime.csv"
df = pd.read_csv(imported_file)

df_trimmed = df[['Community Name', 'Sector', 'Community Center Point']]

df_trimmed.dropna(axis=0, how='any', inplace=True) #Drops NA

print(df_trimmed.head())