# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 09:57:41 2023

@author: Shayan
"""

import pandas as pd
items = pd.DataFrame([{'id':1 ,'name': 'sandals', 'unit price':100 , 'stock':10,'color':{'brown','black'}},
        {'id':2 ,'name': 'sneakers', 'unit price':205 , 'stock':5,'color':{'white','blue'}},
        {'id':3 ,'name': 'high hills', 'unit price':1500 , 'stock':12,'color':{'black','white'}},
        {'id':4 ,'name': 'boots', 'unit price':1800 , 'stock':24,'color':{'brown','black'}},
        {'id':5 ,'name': 'high hills sandals', 'unit price':850, 'stock':9,'color':{'white','black'}}])

items= items.explode('color')