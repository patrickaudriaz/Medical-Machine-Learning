import spacy
from spacy import displacy
import os
import os.path
import json

input = 'input/'
output = 'output/fr/'

nlp = spacy.load("fr")

data = {}
data['MISC'] = []  
data['PER'] = []  
data['LOC'] = []  
data['ORG'] = []  


for path, dir, files in os.walk(input):
    for file in files:
        if file.endswith(".txt"):
            filename = (os.path.join(path, file))
            ocr = open(filename).read()
            doc = nlp(ocr)
            for ent in doc.ents:
              data[ent.label_].append(ent.text)
            #displacy.serve(doc, style="ent")
            if not os.path.exists(output+path):
              os.makedirs(output+path)
            with open(output+filename+'.json', 'w') as json_file:  
              json.dump(data, json_file)