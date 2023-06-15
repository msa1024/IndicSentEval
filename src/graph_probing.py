import matplotlib
matplotlib.use('TkAgg') # or any other backend that works on your system
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

languages = ["telugu","urdu","marathi","malayalam","kannada","hindi"]
tasks = ["senlen","subnum","objnum","treedepth","bshift","wordcontent"]
models = ["multi","indic","xlm","muril"]

def generate_graphs(mbert,indic,xlm,muril,language,task):
    plt.figure()
    plt.plot(np.arange(1,13),np.round(mbert,3))
    plt.plot(np.arange(1,13),np.round(indic,3))
    plt.plot(np.arange(1,13),np.round(xlm,3))
    plt.plot(np.arange(1,13),np.round(muril,3))

    plt.legend(['mbert','IndicBert','XLM','muril'],fontsize = 10)
    plt.xlabel("layer_depth",fontsize = 16)
    plt.ylabel("accuracy",fontsize = 16)
    plt.title(f"{task}",fontsize = 16)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.savefig(f"./results/{language}_{task}_probing.pdf")

for language in languages:
    df = pd.read_csv(f"./results/{language}_probing.csv")
    for task in tasks:
        num_rows = len(df.index)
        my_column_values = df[task].tolist()
        # my_column_values = [eval(i) for i in my_column_values]

        multi = np.array(my_column_values[0:12],dtype='float64')
        indic = np.array(my_column_values[12:24],dtype='float64')
        xlm = np.array(my_column_values[24:36],dtype='float64')
        muril = np.array(my_column_values[36:],dtype='float64')

        generate_graphs(multi,indic,xlm,muril,language,task)

            
            


        

