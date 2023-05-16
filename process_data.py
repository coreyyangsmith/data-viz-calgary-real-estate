#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 15 08:29:35 2023

@author: corey
"""

# Code to process the initial split year files into by-neighbourhood files

import pandas as pd

YEARS = [2005,2006,2007,2008,2009,2010,
         2011,2012,2013,2014,2015,2016,
         2017,2018,2019,2020,2021,2022]

FILE_NAMES = ["year_2005.csv","year_2006.csv","year_2007.csv",
            "year_2008.csv","year_2009.csv","year_2010.csv",
            "year_2011.csv","year_2012.csv","year_2013.csv",
            "year_2014.csv","year_2015.csv","year_2016.csv",
            "year_2017.csv","year_2018.csv","year_2019.csv",
            "year_2020.csv","year_2021.csv","year_2022.csv"]




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

test_file = pd.read_csv(FILE_NAMES[0])
test_file_trimmed = test_file[['ROLL_YEAR', 'ADDRESS', 'ASSESSED_VALUE', 'ASSESSMENT_CLASS', 'COMM_CODE', "COMM_NAME", 'MULTIPOLYGON']]
print(test_file_trimmed.ASSESSMENT_CLASS.value_counts())

print("")
test_file_trimmed = test_file_trimmed[test_file_trimmed["ASSESSMENT_CLASS"].str.contains("RE")==True] #Drops non-res
print(test_file_trimmed.ASSESSMENT_CLASS.value_counts())

test_file_trimmed.dropna(axis=0, how='any', inplace=True) #Drops NA


# Function: Input takes in each year's csv and outputs multiple csv's that are split based on each community's comm_code.
for file_name, year in zip(FILE_NAMES, YEARS):
    current_year = pd.read_csv(file_name)
    current_year_trimmed = current_year[['ROLL_YEAR', 'ADDRESS', 'ASSESSED_VALUE', 'ASSESSMENT_CLASS', 'COMM_CODE', "COMM_NAME", 'MULTIPOLYGON']]
    
    current_year_trimmed = current_year_trimmed[current_year_trimmed["ASSESSMENT_CLASS"].str.contains("RE")==True] #Drops non-res
    current_year_trimmed.drop(['ASSESSMENT_CLASS'], axis=1)  #Drop assessment class
    current_year_trimmed.dropna(axis=0, how='any', inplace=True) #Drops NA
    
    for comm_code in COMM_CODES:
        df_comm_code_location = current_year_trimmed[current_year_trimmed['COMM_CODE'] == comm_code]
        df_comm_code_location.to_csv(str(year) + "/" + comm_code + ".csv")
