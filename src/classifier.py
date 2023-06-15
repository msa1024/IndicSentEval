import codecs,json
import numpy as np
from sklearn.linear_model import LogisticRegression, LogisticRegressionCV
from sklearn.model_selection import train_test_split
import pandas as pd


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
    print(value)

from collections import Counter
bins = create_bins(lower_bound = 15,
                   width = 7,
                   quantity=5)
# bins_len = [(0,15),(16, 22), (23, 29), (30, 36), (37, 43), (44, 50), (51, 57),(58,67),(68,100)]
bins_tree = [(0,2),(3,5),(6,8),(9,11),(12,20)]
bins = [(0,5),(6,8),(9,12),(13,16),(17,20),(21,25),(26,28),(29,1000)]

def getxy(task,language):
    obj_text = codecs.open(f"./gold/{language}/multi_concat_tel_shifted.txt", 'r', encoding='utf-8').read()
    d = json.loads(obj_text) 
    df = pd.read_csv(f"./gold/{language}/{task}.csv")
    y = df[f"{task}"].to_numpy()

    if task == "senlen":
        for i in range(len(y)):
            y[i] = find_bin(y[i],bins)
        return d,y
    

    # For Obj and Sub Number, data needs to be pruned before training the classifier
    elif task == "subnum" or task =="objnum":
        new_d = {}
        for i in np.arange(12):
          new_d[i] = []
        for i in range(0,12):
          for j in range(len(y)):
            if y[j] == "sg" or y[j] == "pl":
              new_d[i].append(d[str(i)][j])

        y_new = []
        for i in range(len(y)):
          if(y[i] == "pl"):
            y_new.append(1)
          elif(y[i] == "sg"):
            y_new.append(0)

        y_new = np.array(y_new)
        return new_d,y_new

    # For WordContent, we need to change input data
    elif task == "wordcontent":
        new_d = {}
        for i in np.arange(12):
          new_d[i] = []
        for i in range(0,12):
          for j in range(len(y)):
            new_d[i].append(d[str(i)][df["index"][j]])
        return new_d,y
    
    else:
        # print(len(d[0]))
        # print(len(y))
        # exit(0)
        return d,y
 

tasks = ["senlen","objnum","subnum","treedepth","wordcontent","bshift"]
# temp = ["str","no","no","str","no","str"]
task = tasks[5]
language = "telugu"
d,y = getxy(task,language)
# print(len(d))
# print(len(y))
# exit(0)


for i in range(0,12):
  X_train, X_test, y_train, y_test = train_test_split(d[str(i)], y, test_size=0.2, random_state=42)

  clf = LogisticRegression(random_state=0, multi_class = "multinomial",max_iter = 250).fit(X_train, y_train)
  # clf = LogisticRegressionCV(cv=5,random_state=0,max_iter=1000).fit(np.array(d[i]), y)

  print(i, clf.score(X_test, y_test))

