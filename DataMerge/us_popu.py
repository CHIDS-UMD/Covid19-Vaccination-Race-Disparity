import pandas as pd
import numpy as np


def get_county_id(v):
    v = str(v)
    if len(v) == 1:
        return '00' + str(v)
    elif len(v) == 2:
        return '0' + str(v)
    elif len(v) == 3:
        return v
    else:
        raise ValueError('Error')
    
def get_state_id(v):
    v = str(v)
    if len(v) == 1:
        return '0' + str(v)
    elif len(v) == 2:
        return v
    else:
        raise ValueError('Error')
    
    


def remove_string(s):
    return s.replace(' County', '')

def get_county(s):
    return s.split(', ')[0]

def get_state(s):
    return s.split(', ')[1]

def getGEOID(idx):
    return idx.split('US')[-1]


def change_col_name(name):
    d = {}
    
    d['TOT_POP'] = 'Total_Whole'
    d['WA'] = 'Total_White'
    d['BA'] = 'Total_Black'
    d['IA'] = 'Total_AIndA'
    d['AA'] = 'Total_Asian'
    
    for k, v in d.items():
        if k in name:
            name = name.replace(k, v)
    
    return name



def get_US_COUNTY_POPULATION(path_cc, path_acs):
    # path_cc = 'Data/cc-est2019-alldata.csv'

    CCALLDATA = pd.read_csv(path_cc)

    CCALLDATA = CCALLDATA[CCALLDATA['YEAR'] == 12]  # 12: 2019-7-1
    CCALLDATA = CCALLDATA[CCALLDATA['AGEGRP'] == 0] #  0: Age Group Total
    CCALLDATA = CCALLDATA[CCALLDATA['SUMLEV'] == 50] #  50: County and/or Statistical Equivalent
    CCALLDATA = CCALLDATA.reset_index(drop = True)


    CCALLDATA['GEOID'] = CCALLDATA['STATE'].apply(get_state_id) + CCALLDATA['COUNTY'].apply(get_county_id)
    # POPULATION

    PrefixCols = ['GEOID', 'TOT_POP'] 
    RaceCols = ['WA', 'BA', 'NHWA', 'NHBA']

    for i in RaceCols:

        CCALLDATA[i] = CCALLDATA[i + '_MALE'] + CCALLDATA[i +'_FEMALE']


    CCALLDATA = CCALLDATA[PrefixCols + RaceCols]

    # print(CCALLDATA.shape)
    # CCALLDATA.head()
    
    INTERNET_SUBSCRIPTIONS = pd.read_csv(path_acs, skiprows=[0], low_memory=False)[['id', 'Geographic Area Name'] ]
    # How to understand total population in household?


    INTERNET_SUBSCRIPTIONS['Geographic Area Name'] = INTERNET_SUBSCRIPTIONS['Geographic Area Name'].apply(remove_string)
    INTERNET_SUBSCRIPTIONS['County'] = INTERNET_SUBSCRIPTIONS['Geographic Area Name'].apply(get_county)
    INTERNET_SUBSCRIPTIONS['State']  = INTERNET_SUBSCRIPTIONS['Geographic Area Name'].apply(get_state)



    INTERNET_SUBSCRIPTIONS['GEOID'] = INTERNET_SUBSCRIPTIONS['id'].apply(getGEOID)
    INTERNET_SUBSCRIPTIONS = INTERNET_SUBSCRIPTIONS[['GEOID', 'State', 'County', 'Geographic Area Name', ]]
    # print(INTERNET_SUBSCRIPTIONS.shape)
    # INTERNET_SUBSCRIPTIONS.head()



    US_COUNTY_POPULATION = pd.merge(INTERNET_SUBSCRIPTIONS, CCALLDATA, on = 'GEOID')

    cols_dict = {name: change_col_name(name) for name in US_COUNTY_POPULATION.columns}

    US_COUNTY_POPULATION = US_COUNTY_POPULATION.rename(columns = cols_dict)


    # print(US_COUNTY_POPULATION.shape)
    # US_COUNTY_POPULATION.head()
    
    
    return US_COUNTY_POPULATION


