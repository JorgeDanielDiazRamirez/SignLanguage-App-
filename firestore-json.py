import os, sys
import json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from itertools import groupby
import timeit

# Use a service account.
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'asl-machinelearning-367219-ffcc57e6b3b4.json'
cred = credentials.Certificate('asl-machinelearning-367219-ffcc57e6b3b4.json')

app = firebase_admin.initialize_app(cred)

#firebase_admin.initialize_app(cred, {
#'projectId': "asl-machinelearning-367219",
#})

dbnosql = firestore.client()

json_labels_file_path =  "./json-training-labels/" #Editar

#json_file_path = os.path.join(json_labels_file_path, "a-createml.json")#"./myfile.json" 
json_file_path = "./json-training-labels/a-createml.json"

with open(json_file_path, 'r') as j:
    contents = json.loads(j.read())

jsonFile = open('./json-training-labels/a-createml.json')
data = json.load(jsonFile)


doc_ref = dbnosql.collection(u"Training-labels").document(u"Labels")

for filename in os.listdir(json_labels_file_path):

    if filename.endswith('.json'):

        collectionName = filename.split('.')[0] # filename minus ext will be used as collection name

        f = open(json_labels_file_path + filename, 'r')

        docs = json.loads(f.read())

        for doc in docs:

            id = doc.pop('id', None)

            if id:

                dbnosql.collection(collectionName).document(id).set(doc, merge=True)

            else:

                dbnosql.collection(collectionName).add(doc)