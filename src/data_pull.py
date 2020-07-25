import numpy as np
import pandas as pd

# Requests sends and recieves HTTP requests.
import requests


import json
import time
import copy 


#pull census variables 
#storing census variable names(unreadable) with readable column names 
var_req = requests.get('https://api.census.gov/data/2018/acs/acs1/spp/variables.json').json()


col_name = {}
variables = var_req['variables']

for k, v in variables.items():
    col_name[k] = v['label']
    

#remove all the columns that have PR in them
clean_col_name = col_name.copy()
stat = 'PR'


for k, v in col_name.items():
    if stat in k:
        del clean_col_name[k]


#flexible pull request for api call, generates names for api url
def census_name_pull(name_dict, word_search):
    name_list = ['NAME','GEO_ID']


    for k, v in name_dict.items():
        if word_search in v:
            name_list.append(k)
    return sorted(name_list)


#connect to api_url for census per 
# get_vars = [sex_age_pull, emp_stat_pull, industry_pull, income_pull]

def api_pull_request(get_vars):

    api_key = 'ce30285f0f2fedc096b5bf054c7d573ea6558309'
    base_url = 'https://api.census.gov/data/2018/acs/acs1/spp?'

    predicates = {}
    predicates['get'] = ','.join(get_vars)
    predicates['for'] = 'county:*'
    predicates['in'] = 'state:*'
    predicates['key'] = api_key
    
    r = requests.get(base_url, params=predicates)
    
    return r.json()