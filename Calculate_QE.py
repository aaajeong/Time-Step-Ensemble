#!/usr/bin/env python
# coding: utf-8

# In[1]:


import torch
import openpyxl
import numpy as np 
# from tqdm import tqdm
from tqe import TQE


# In[ ]:


wb = openpyxl.load_workbook('TQE(Epoch).xlsx')
sheet = wb['model_5']
# source : 번역 원문
# target : 기계 번역 문장

for i in range(500, 1002):
    target = []
    source = []
    candidate = sheet.cell(row = i, column = 19).value.capitalize()
    reference = sheet.cell(row = i, column = 3).value
    print(i, ':', candidate)

    # Translation Quality Estimator (QE)
    # https://github.com/theRay07/Translation-Quality-Estimator
    target.append(candidate)
    source.append(reference)
    model = TQE('LaBSE')
    cos_sim_values = model.fit(source, target)
    sheet.cell(row = i, column = 20).value = cos_sim_values[0]
    
wb.save('TQE(Epoch).xlsx')


# lang_1 = ["my son s name is tom ."]
# lang_2 = ["El nombre de mi hijo es Tom."]

# model = TQE('LaBSE')
# cos_sim_values = model.fit(lang_1, lang_2)
# print(cos_sim_values)


# In[ ]:


# wb = openpyxl.load_workbook('TQE(Epoch).xlsx')
# sheet = wb['model_1']
# qe = []


# for i in range(2, 1002):
#     qe.append(float(sheet.cell(row = i, column = 5).value))

    
# qe = np.array(qe)

# sheet.cell(row = 1002, column = 5).value = qe.mean()


# wb.save('TQE(Epoch).xlsx')

