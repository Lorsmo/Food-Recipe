#--Injest--

import os
import re
import pymongo
import json
from bson import json_util, ObjectId
from bson.json_util import dumps
import requests

#import pandas as pd
from ast import literal_eval

data_path = 'static/data/'

def injest():
    mydb = myclient["finalproject"]
    mycol = mydb["recipes"]
    mycol.drop()

    entry_dict = {}
    print('begin db entries...')

    for filename in os.listdir(data_path):
        file_path = data_path + filename
        file_obj = open(file_path,"r") 
        temp1 = file_obj.read()
        temp2 = literal_eval(temp1)
        
        for i in range(len(temp2)):    
            try:
                name = re.search(r'(?<=\|NAME:)[^|]*',temp2[i]).group()
            except:
                name = 'None'
            try:
                desc = re.search(r'(?<=\|DESC:)[^|]*',temp2[i]).group()
            except:
                desc = 'None'           
            try:
                ingredients = re.search(r'(?<=\|INGREDIENTS:)[^|]*',temp2[i]).group()
            except:
                ingredients = 'None'            
            try:
                steps = re.search(r'(?<=\|STEPS:)[^|]*',temp2[i]).group()           
            except:
                steps = 'None'            

            entry_dict['name'] = name
            entry_dict['desc'] = desc
            entry_dict['ingredients'] = ingredients
            entry_dict['steps'] = steps
            
            with open('temp.json', 'w') as fp:
                json.dump(entry_dict, fp)
            with open('temp.json') as J:
                file_data = json.load(J)
            mycol.insert_one(file_data) #insert entry into MongoDB
            print(f"Inserted: {name}")
    
    print('...db entries done')
    myclient.close()

MONGO_URL = "mongodb+srv://danh:pJmVMOcSjYNZ87rt@cluster0-zhzxw.mongodb.net/test?retryWrites=true&w=majority"
myclient = pymongo.MongoClient(MONGO_URL, maxPoolSize=50, connect=True)
injest()