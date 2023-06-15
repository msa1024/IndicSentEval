import matplotlib
matplotlib.use('TkAgg') # or any other backend that works on your system
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os

languages = ["telugu","urdu","marathi","malayalam","kannada","hindi"]
tasks = ["senlen","subnum","objnum","treedepth"]
models = ["xlm","multi","indic","muril"]
perturbations = ["appendirr","dropallboth","dropallNN","dropallVB","dropfirst","dropfirstlast","droplast","droprandNN","droprandVB","keepboth","keepNN","keepVB","shuffle"]

def get_accuracies(perturbation, task,df):
    perturbation_col = df[perturbations.index(perturbation) * 12 : (perturbations.index(perturbation) + 1) * 12]
    return perturbation_col[task].tolist()

def generate_graphs(xlm,mbert,indic,muril,language,task,perturbation):
    plt.figure()
    plt.plot(np.arange(1,13),np.round(xlm,3))
    plt.plot(np.arange(1,13),np.round(mbert,3))
    plt.plot(np.arange(1,13),np.round(indic,3))
    plt.plot(np.arange(1,13),np.round(muril,3))

    plt.legend(['XLM','mbert','IndicBert','muril'],fontsize = 10)
    plt.xlabel("layer_depth",fontsize = 16)
    plt.ylabel("accuracy",fontsize = 16)
    plt.title(f"{task}",fontsize = 16)
    plt.xticks(fontsize = 16)
    plt.yticks(fontsize = 16)
    plt.savefig(f"./results/perturbations/{language}_{perturbation}_{task}.pdf")
    plt.close()

def splitcsv(xlm,mbert,indic,muril,language,task,perturbation):
    dict = {"score":xlm}
    df = pd.DataFrame(dict)
    df.to_csv(f"./results/perturbations/perturbations_old/{language}/xlm_{task}_{perturbation}.csv")
    dict = {"score":mbert}
    df = pd.DataFrame(dict)
    df.to_csv(f"./results/perturbations/perturbations_old/{language}/mbert_{task}_{perturbation}.csv")
    dict = {"score":indic}
    df = pd.DataFrame(dict)
    df.to_csv(f"./results/perturbations/perturbations_old/{language}/indic_{task}_{perturbation}.csv")
    dict = {"score":muril}
    df = pd.DataFrame(dict)
    df.to_csv(f"./results/perturbations/perturbations_old/{language}/muril_{task}_{perturbation}.csv")

for language in languages[5:]:
    df = pd.read_csv(f"./results/{language}_per.csv")
    df_xlm = df.iloc[0:156]
    df_multi = df.iloc[156:312]
    df_indic = df.iloc[312:468]
    df_muril = df.iloc[468:]
    # print(len(df_xlm))
    # print(len(df_multi))
    # print(len(df_indic))
    # print(len(df_muril))
    # print(get_accuracies("shuffle","treedepth",df_indic))

    for perturbation in perturbations:
        if language == "kannada":
            tasks = ["senlen","treedepth"]
        for task in tasks:

            xlm = np.array(get_accuracies(perturbation,task,df_xlm),dtype="float64")
            multi = np.array(get_accuracies(perturbation,task,df_multi),dtype="float64")
            indic = np.array(get_accuracies(perturbation,task,df_indic),dtype="float64")
            muril = np.array(get_accuracies(perturbation,task,df_muril),dtype="float64")

            splitcsv(xlm,multi,indic,muril,language,task,perturbation)
            
            


        

