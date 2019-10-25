import json
import textdistance
import operator
import os
import os.path
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

input = 'input/'

########################

doctorNom = []
doctorPrenom = []

jsonMedFile = json.loads(open('med.json').read())

for key, doctor in enumerate(jsonMedFile):
  doctorNom.append(doctor["MedNom"])
for key, doctor in enumerate(jsonMedFile):
  doctorPrenom.append(doctor["MedPrenom"])

########################

patientNom = []
patientPrenom = []

jsonPatFile = json.loads(open('pat.json').read())

for key, patient in enumerate(jsonPatFile):
  patientNom.append(patient["PatNom"])
for key, patient in enumerate(jsonPatFile):
  patientPrenom.append(patient["PatPrenom"])

########################

stringToFind = []

for i in range(len(jsonMedFile)) :
  stringToFind.append(str(jsonMedFile[i]["MedNom"][0]).lower())

########################

for path, dir, files in os.walk(input):
    for file in files:
        if file.endswith(".txt"):
            filename = (os.path.join(path, file))
            dataFile = open(filename, 'r')
            results = []
            for line in dataFile :
              for word in line.split():
                for e in stringToFind:
                  # Fuzzy string matching with Jaro Distance
                  if (textdistance.jaro.normalized_similarity(word.lower(), e) > 0.7):
                    print("search : ", e)
                    print("found : " + word)
                    print("score : ", textdistance.jaro.normalized_similarity(word.lower(), e))
                    print("file : ", filename)
                    print("----------------------------")
