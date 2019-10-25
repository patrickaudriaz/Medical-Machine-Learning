import json
from fuzzywuzzy import fuzz
from fuzzywuzzy import process
import operator
import os
import os.path

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
            for line in dataFile :
              for word in line.split():
                for e in stringToFind:
                  # Fuzzy string matching with Levenshtein Distance
                  if (fuzz.token_sort_ratio(word.lower(), e) > 60):
                    print("search : ", e)
                    print("found : " + word)
                    print("score : ", fuzz.token_sort_ratio(word.lower(), e))
                    print("file : ", filename)
                    print("----------------------------")
