############
import os
import pymongo
import json
from bson import json_util, ObjectId
from bson.json_util import dumps
import requests
from flask import Flask, render_template, Markup, request, redirect, jsonify

############
# import zipfile
# import pathlib
# from pathlib import Path
# ############
# from collections import defaultdict
import re
# import string
# ############
# import pandas as pd
# from datetime import datetime
# ############
# import heapq


# Create an instance of Flask
app = Flask(__name__)
MONGO_URL = os.environ.get('MONGO_URL')

myclient = pymongo.MongoClient(MONGO_URL, maxPoolSize=50, connect=True)
# stuff = {'text':'BLANK','count':0}
# data_path = 'static/data/'
# unzip_path = 'static/data/unzip/'



@app.route('/', methods=['GET', 'POST', 'OPTIONS'])
def home():
    """Landing page."""
    return render_template("index.html")



@app.route("/readfull/<search_word>")
def finddocs(search_word):

    print('Starting query...')
    print(search_word)
    mydb = myclient["finalproject"]
    mycol = mydb["recipes"]
    
    ############
    myquery =  {"name" : { '$regex' : search_word }}
    ############

    cursor = json.loads(dumps(mycol.find(myquery)))

    myclient.close()
    print(jsonify(list(cursor)))

    return jsonify(list(cursor))

@app.route('/team', methods=['GET', 'POST'])
def team():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('team.html')

@app.route('/index', methods=['GET', 'POST'])
def team():
    if request.method == 'POST':
        # do stuff when the form is submitted

        # redirect to end the POST handling
        # the redirect can be to the same route or somewhere else
        return redirect(url_for('index'))

    # show the form, it wasn't submitted
    return render_template('team.html')

@app.route("/injest")
def injest():
    # ### unzip files
    # pathlib.Path(unzip_path).mkdir(parents=False, exist_ok=True)
    # with zipfile.ZipFile(f'{data_path}/data.zip', 'r') as zip_ref:
    #     zip_ref.extractall(unzip_path)
    # ###
    mydb = myclient["finalproject"]
    mycol = mydb["recipes"]
    # mycol.drop()

    # #get directory/object structure from _dir.csv file
    # with open(f'{unzip_path}/_dir.csv', 'r', encoding='utf8') as docpath:
    #     df = pd.read_csv(docpath, header=0)

    # os.remove(f'{unzip_path}/_dir.csv') #delete _dir.csv
    # #os.rename(f'{unzip_path}/_dir.csv', 'static/data/_dir.csv') #move _dir.csv
    
    # entry_dict = {}
    print('begin db entries...')

    # for (root,dirs,files) in os.walk(unzip_path, topdown=True):
    for files in os.path(datapath):
    #     if files != [] :
    #         dirname = str(root.split("\\")[-1])
            
    #         #interpret info from _dir.csv for object keys
    #         for colname in df.columns:
    #             row = df.loc[df['_dir'] == dirname].index.values.astype(int)[0]
    #             entry_dict[colname] = str(df.at[row,colname])
    #         entry_dict['_dir'] = root
    #         #######
    #         for (file) in files:
    #             filename = str(Path(file).with_suffix(''))
    #             entry_dict['filename'] = filename
            
    #             docpath = open(f'{root}/{file}', 'r', encoding='utf8')
    #             fulltext = docpath.read()
            
    #             try:
    #                 doctitle = re.search('<title="(.*)">', fulltext).group(1)
                        name = re.search('|NAME(.*)|', fulltext).group(1)
                        doctitle = re.search('<title="(.*)">', fulltext).group(1)
    #             except:
    #                 doctitle = ''
    #             try:
    #                 docdate_long = re.search('<date="(.*)">', fulltext).group(1)
    #                 docdate = datetime.strftime(datetime.strptime(docdate_long,'%B %d, %Y'), '%Y/%m/%d')
    #             except:
    #                 docdate = ''
    #             entry_dict['title'] = doctitle
    #             entry_dict['date_ymd'] = docdate
    #             entry_dict['date'] = docdate_long

    #             #remove title, date, newlines, punctuation marks
    #             proc1 = re.sub('<.+>', '', fulltext).lower().strip('\n\r')
    #             bodytext = proc1.translate({ord(i): None for i in '.,;:?!-=+''"()[]''{''}$&'''})
    #             words_list = str.split(bodytext)
                
    #             freq_dict = defaultdict(int)
    #             stopwords = ['which','or','are','and', 'it', 'that', 'is', 'be', 'being', 'been', 'not', 'this', 'i', 'was', 'have', 'a','aboard','about','above','across','after','against','along','amid','among','an','anti','around','as','at','away','before','behind','below','beneath','beside','besides','between','beyond','but','by','concerning','considering','despite','down','during','except','excepting','excluding','following','for','from','in','inside','into','like','minus','near','next','of','off','on','onto','opposite','out','outside','over','past','per','plus','regarding','round','save','since','than','the','through','til','till','to','toward','towards','under','underneath','unlike','until','up','upon','versus','via','with','within','without']

                
    #             for word in words_list:
    #                 if word not in stopwords:
    #                     freq_dict[word] += 1
                
    #             freqs_list = []
    #             for key in freq_dict:
    #                 temp_d = {}
    #                 temp_d['word'] = key
    #                 temp_d['count'] = freq_dict[key]
    #                 freqs_list.append(temp_d)

    #             entry_dict['word_counts'] = freqs_list
                
    #             with open(f'{unzip_path}../temp.json', 'w') as fp:
    #                 json.dump(entry_dict, fp)
    #             with open(f'{unzip_path}../temp.json') as J:
    #                 file_data = json.load(J)
    #             mycol.insert_one(file_data)
    #             print(f"Inserted: {filename}")
    
    # print('...db entries done')
    # myclient.close()
    
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
