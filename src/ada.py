import torch
from transformers import BertTokenizer, BertModel, AutoTokenizer, AutoModelForSeq2SeqLM, AlbertTokenizer, AutoModelForMaskedLM
import re
import numpy as np
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.model_selection import train_test_split
import pandas as pd
import numpy as np
import json

language = ""
model_name = "ai4bharat/indic-bert"
sen_filepath = "./gold/malayalam/sentences.txt"
shifted_sen_filepath = "./gold/malayalam/shifted_sentences.txt"
outpath= f"./gold/{language}/indic_concat_{str(language)[:3]}.txt"


tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForMaskedLM.from_pretrained("ai4bharat/indic-bert")
print("MODEL LOADED !")

sentences = []
with open(sen_filepath, "r") as f:
  while True:
    sentence = f.readline()
    sentence = sentence.strip()
    if len(sentence) == 0:
      break
    re.sub("\n","", sentence)
    temp = "[CLS] "+ sentence +" [SEP]"
    sentences.append(str(temp))

shifted_sentences = []
with open(shifted_sen_filepath, "r") as f:
  while True:
    sentence = f.readline()
    sentence = sentence.strip()
    if len(sentence) == 0:
      break
    re.sub("\n","", sentence)
    temp = "[CLS] "+ sentence +" [SEP]"
    shifted_sentences.append(str(temp))

print("FILES LOADED!")

count  = 0
d = {}
for i in np.arange(12):
  d[str(i)] = []

for sentence in sentences:
  if count%100 == 1:
    print(count)
  count += 1
  inputs = tokenizer(sentence, return_tensors="pt",max_length=512)
  features = model(**inputs, output_hidden_states=True)
  for i in range(0,12):
    d[str(i)].append(features['hidden_states'][i][0][0].detach().numpy().tolist())

print("FEATURES LOADED!")

with open(, 'w') as convert_file:
     json.dump(dict(d), convert_file)

print("FEATURES WRITTEN")
exit(0)


def create_bins(lower_bound, width, quantity):
    bins = []
    for low in range(lower_bound, 
                     lower_bound + quantity*width + 1, width):
        bins.append((low, low+width)) 
    return bins

def find_bin(value, bins):
    for i in range(0, len(bins)):
        if bins[i][0] <= value <= bins[i][1]:
            return i

from collections import Counter
bins = create_bins(lower_bound = 15,
                   width = 7,
                   quantity=5)

# print(bins)
# bins_len = [(0,15),(16, 22), (23, 29), (30, 36), (37, 43), (44, 50), (51, 57),(58,67),(68,100)]
bins_tree = [(0,2),(3,5),(6,8),(9,11),(12,20)]
bins = [(0,5),(6,8),(9,12),(13,16),(17,20),(21,25),(26,28),(29,200)]


df = pd.read_csv("./gold/marathi/senlen.csv")

y = df["len"].to_numpy()
for i in range(len(y)):
  y[i] = find_bin(y[i],bins)

# For Obj and Sub Number, data needs to be pruned before training the classifier

# new_d = {}
# for i in np.arange(12):
#   new_d[i] = []
# for i in range(0,12):
#   for j in range(len(y)):
#     if y[j] == "sg" or y[j] == "pl":
#       new_d[i].append(d[i][j])
  

# y_new = []
# for i in range(len(y)):
#   if(y[i] == "pl"):
#     y_new.append(1)
#   elif(y[i] == "sg"):
#     y_new.append(0)

# print(len(y_new))
# print(len(new_d[0]))

# y_new = np.array(y_new)

# For WordContent, we need to change input data
# new_d = {}
# for i in np.arange(12):
#   new_d[i] = []
# for i in range(0,12):
#   for j in range(len(y)):
#     new_d[i].append(d[i][df["index"][j]])  

# print(len(y))
# print(len(d[0]))

for i in range(0,12):
  X_train, X_test, y_train, y_test = train_test_split(d[str(i)], y, test_size=0.2, random_state=42)

  clf = LogisticRegression(random_state=0, multi_class = "multinomial",max_iter = 250).fit(X_train, y_train)
  # clf = LogisticRegressionCV(cv=5,random_state=0,max_iter=1000).fit(np.array(d[i]), y)

  print(i, clf.score(X_test, y_test))

print("JOB DONE!")
