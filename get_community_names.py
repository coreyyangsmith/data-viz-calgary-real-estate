#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 17:33:24 2023

@author: corey
"""

import pandas as pd

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

COMM_CODES.sort()

print(len(COMM_CODES))

import_file = "year_2014.csv"
df = pd.read_csv(import_file)

df_trimmed = df[['COMM_CODE', 'COMM_NAME']]

my_dictionary = {}

for i in COMM_CODES:
    comm_df = df_trimmed[df_trimmed["COMM_CODE"] == i]
    community_name = comm_df['COMM_NAME'].iloc[0]
    
    my_dictionary[i] = community_name

for i,j in my_dictionary.items():
    print(i,j)
    
    