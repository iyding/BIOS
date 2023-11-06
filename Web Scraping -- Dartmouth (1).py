#!/usr/bin/env python
# coding: utf-8

# In[222]:


# Sports Analytics: Ivy League
# Note: the data is from 2023; I scraped the Dartmouth Football 2023 roster into a dataframe just to try it out,
# maybe the code will be useful for other schools


# In[223]:


import requests
from bs4 import BeautifulSoup
import pandas as pd

import matplotlib.pyplot as plt
import pandas as pd
import time
import re

from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver

from IPython.display import display, Image


# In[224]:


b = webdriver.Chrome()
url = "https://dartmouthsports.com/sports/football/roster"
b.get(url)


# In[257]:


#finding the column names to construct a data frame
#tbh I don't really use this cell later on, but kept just in case
tbl = b.find_elements("tag name", "tr")

column_names = []


for rows in tbl:
    cells = rows.find_elements("tag name", "td")
    for cell in cells:
        name = cell.get_attribute("class")
        
        if name not in column_names:
            # the line below is hardcoding??? point is I don't want these in the dataframe
            if name != "image_combined_path noprint" and name != "" and name != "image_combined_path hide-on-small-down noprint":
                column_names.append(name)
            else:
                continue

column_names 


# In[243]:


#list containing information for each player

info = []

body = b.find_elements("tag name", "tbody")

#there are 3 tables on the webpage; only want the first one containing player information
t = body[0]

tbl = t.find_elements("tag name", "tr")

for rows in tbl:
    cells = rows.find_elements("tag name", "td")
    for cell in cells:
        info.append(cell.text)
info
 


# In[273]:


#creating dataframe

#create dictionary first
data = {}
data["jersey"] = [info[num] for num in range(0,len(info),8)]
data["names"] = [info[num] for num in range(1,len(info),8)]
data["position"] = [info[num] for num in range(2,len(info),8)]
data["height"] = [info[num] for num in range(3,len(info),8)]
data["weight"] = [info[num] for num in range(4,len(info),8)]
data["year"] = [info[num] for num in range(5,len(info),8)]
data["highschool"] = [info[num] for num in range(6,len(info),8)]
data["hometown"] = [info[num] for num in range(6,len(info),8)]



df = pd.DataFrame(data)
df.set_index("jersey")
 
    


# In[274]:


b.quit()


# In[ ]:


#Data Analysis

# What are the Geographic, socio-economic, social and demographic characteristics of their communities?

# What are the characteristics of their highschools (school size, urban/rural/suburban classification, 
# student demographics, title 1 status)?

# What other interesting trends can you find?

