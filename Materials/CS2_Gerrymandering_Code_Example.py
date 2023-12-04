#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd 
from PIL import Image, ImageColor
from scipy.stats import chi2_contingency
import math


# In[ ]:


# import image of VA with current districts
VA_current = Image.open("C:/Users/rheas/OneDrive/Pictures/Camera Roll\VA_current.png")

# find pixel counts of each color in image
VA_current_lis = VA_current.getcolors(maxcolors=10000)
print(VA_current_lis)


# In[ ]:


# calculate counts of red, purple, and blue in image
light red = (249, 139, 136, 255)(249,144,141,255)
medium red = (249,115,110,255)
dark red = (248,80,72,255)(248,71,64,255)
purple = (204, 38, 195, 255)
light blue = (114,146,255,255)
dark blue = (85,124,255,255)(86,125,255,255)(81,121,255,255)


# In[20]:


VA_current_lightred = (22656 + 6440)
VA_current_mediumred = 9561
VA_current_darkred = (13372 + 21524)
VA_current_purple = 5743
VA_current_lightblue = 8387
VA_current_darkblue = (1361 + 180)

print(VA_current_lightred)
print(VA_current_mediumred)
print(VA_current_darkred)
print(VA_current_purple)
print(VA_current_lightblue)
print(VA_current_darkblue)


# In[ ]:


# import image of VA with proportionally partisan districts
VA_prop_part = Image.open("C:/Users/rheas/Downloads/VA_prop_part.png")

# find pixel counts of each color in image
VA_prop_part_lis = VA_prop_part.getcolors(maxcolors=10000)
print(VA_prop_part_lis)


# In[ ]:


# calculate percentage of red, purple, and blue in image
light red = (249,148,145,255)
medium red = 
dark red = (248,90,83,255)(248,83,75,255)(248,93,87,255)(248,71,63,255)
purple = (204, 38, 195, 255)
dark blue = (88,126,255,255)(81,121,255,255)(95,132,255,255)
light blue = (121,151,255,255)(139,166,255,255)


# In[21]:


VA_prop_part_lightred = 9229 
VA_prop_part_mediumred = 0 
VA_prop_part_darkred = (10612 + 14907 + 19476 + 21534)
VA_prop_part_purple = 5474
VA_prop_part_lightblue = (514 + 207 + 489) 
VA_prop_part_darkblue = (7501 + 891)

print(VA_prop_part_lightred)
print(VA_prop_part_mediumred)
print(VA_prop_part_darkred)
print(VA_prop_part_purple)
print(VA_prop_part_lightblue)
print(VA_prop_part_darkblue)


# In[22]:


# defining the table
data = [[VA_current_lightred, VA_current_mediumred, VA_current_darkred, VA_current_purple, VA_current_lightblue, VA_current_darkblue],[VA_prop_part_lightred, VA_prop_part_mediumred, VA_prop_part_darkred, VA_prop_part_purple, VA_prop_part_lightblue, VA_prop_part_darkblue]]
stat, p, dof, expected = chi2_contingency(data)
   
# interpret p-value
alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (H0 holds true)')


# In[ ]:


# import image of NM with current districts
NM_current = Image.open("C:/Users/rheas/OneDrive/Pictures/Screenshots/NM_current.png")

# find pixel counts of each color in image
NM_current_lis = NM_current.getcolors(maxcolors=10000)
print(NM_current_lis)


# In[23]:


NM_current_mediumred = 420477
NM_current_lightblue = 420477


# In[ ]:


# import image of NM with proportionally partisan districts
NM_prop_part = Image.open("C:/Users/rheas/OneDrive/Pictures/Screenshots/NM_nogerry.png")

# find pixel counts of each color in image
NM_prop_part_lis = NM_prop_part.getcolors(maxcolors=10000)
print(NM_prop_part_lis)


# In[24]:


NM_prop_part_mediumred = 673524
NM_prop_part_lightblue = 39773


# In[25]:


# defining the table
data = [[NM_current_mediumred, NM_current_lightblue],[NM_prop_part_mediumred, NM_prop_part_lightblue]]
stat, p, dof, expected = chi2_contingency(data)
   
# interpret p-value
alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (H0 holds true)')


# In[ ]:


# import image of MA with current districts
MA_current = Image.open("C:/Users/rheas/OneDrive/Pictures/Screenshots/MA_current.png")

# find pixel counts of each color in image
MA_current_lis = MA_current.getcolors(maxcolors=10000)
print(MA_current_lis)


# In[26]:


MA_current_darkblue = 28352
MA_current_lightblue = 58042
MA_current_blue = 181195
MA_current_purple = 141046


# In[ ]:


# import image of MA with proportionally partisan districts
MA_prop_part = Image.open("C:/Users/rheas/OneDrive/Pictures/Screenshots/MA_nogerry.png")

# find pixel counts of each color in image
MA_prop_part_lis = MA_prop_part.getcolors(maxcolors=10000)
print(MA_prop_part_lis)


# In[27]:


MA_prop_part_darkblue = 37
MA_prop_part_lightblue = 94
MA_prop_part_blue = 181195
MA_prop_part_purple = 19


# In[28]:


# defining the table
data = [[MA_current_darkblue, MA_current_lightblue, MA_current_blue, MA_current_purple],[MA_prop_part_darkblue, MA_prop_part_lightblue, MA_prop_part_blue, MA_prop_part_purple]]
stat, p, dof, expected = chi2_contingency(data)
   
# interpret p-value
alpha = 0.05
print("p value is " + str(p))
if p <= alpha:
    print('Dependent (reject H0)')
else:
    print('Independent (H0 holds true)')


# In[ ]:


# AL current

AL_current = Image.open("C:/Users/rheas/OneDrive/Pictures/Screenshots/AL_current.png")

# find pixel counts of each color in image
AL_current_lis = AL_current.getcolors(maxcolors=10000)
print(AL_current_lis)


# In[ ]:


#AL no gerry
AL_prop_part = Image.open("C:/Users/rheas/OneDrive/Pictures/Screenshots/AL_nogerry.png")

# find pixel counts of each color in image
AL_prop_part_lis = AL_prop_part.getcolors(maxcolors=10000)
print(AL_prop_part_lis)


# In[ ]:


# Nevada current
Nevada_current = Image.open("C:/Users/rheas/OneDrive/Pictures/Screenshots/Nevada_current.png")

# find pixel counts of each color in image
Nevada_current_lis = Nevada_current.getcolors(maxcolors=10000)
print(Nevada_current_lis)


# In[ ]:


#Nevada no gerry
Nevada_prop_part = Image.open("C:/Users/rheas/OneDrive/Pictures/Screenshots/Nevada_nogerry.png")

# find pixel counts of each color in image
Nevada_prop_part_lis = Nevada_prop_part.getcolors(maxcolors=10000)
print(Nevada_prop_part_lis)


# In[18]:


# declination angle: severity of the angle corresponds directly with the severity of the gerrymander
# pass list of democratic vote share in each district

def calculate_declination_angle(dem_vote_share):
   majority_wins = sorted(filter(lambda x: x <= 0.5, dem_vote_share))
   minority_wins = sorted(filter(lambda x: x > 0.5, dem_vote_share))
   theta = np.arctan((1 - 2 * np.nanmean(majority_wins)) * len(dem_vote_share) / len(majority_wins))
   gamma = np.arctan((2 * np.nanmean(minority_wins)-1) * len(dem_vote_share) / len(minority_wins))
   declination_angle = 2 * (gamma - theta) / np.pi
   return declination_angle


# In[19]:


# declination angle VA
calculate_declination_angle([44.14, 48.27, 67.22, 65.74, 43.87, 37.29, 51.13, 74.95, 29.11, 55.2, 67.34])


# In[ ]:


# declination angle NM
calculate_declination_angle([54.38, 52.34, 55.23])


# In[ ]:


# declination angle MA
calculate_declination_angle([55.49,58.24,56.8,57.51,68.24,55.94,81.41,60.19])


# In[ ]:


# decliantion angle Nevada
calculate_declination_angle([52.62,40.47,51.74,52.61])

