# -*- coding: utf-8 -*-
"""
Created on Mon May  1 14:58:24 2023

@author: Madhavan
"""
import re
import json
def clean_text(tamil_text):
    # Remove newline characters and commas
    tamil_text = re.sub(r'[\n,]', '', tamil_text)
    # Remove digits
    tamil_text = re.sub(r'\d+', '', tamil_text)
    # Remove English characters
    tamil_text = re.sub(r'[a-zA-Z]+', '', tamil_text)
    tamil_text = re.sub(r'[^\u0B80-\u0BFF\s]', '', tamil_text)
    return tamil_text
    
with open('abirami_anthathi.txt','r',encoding='utf-8') as f:
    data = f.readlines()
m = 0
ls = []
for i in data:
    if i[0].isdigit():
        ls.append(m)
    m+=1
ls.append(len(data))
n = 0

ls1 = []
while n<len(ls)-1:
    mydict = {}
    venba = ""
    urai = ""
    rng1 = range(ls[n],ls[n]+4)
    rng2 = range(ls[n]+5,ls[n+1])
    for k in rng1:
        venba = venba + data[k]
    for l in rng2:
        urai = urai + data[l]
    mydict["poem"] = clean_text(venba)
    mydict["description"] = clean_text(urai)
    print(mydict)
    n+=1
    ls1.append(mydict)
with open("output/abirami_anthathi.json", "w", encoding="utf-8") as f:
    json.dump(ls1, f, ensure_ascii=False, indent=4)
        

