import pandas as pd
import os
import csv
import numpy as np

languages = ["telugu","hindi","marathi","kannada","urdu","malayalam"]
tasks = ["senlen","subnum","objnum","treedepth","bshift","wordcontent"]

for language in languages:
    df1 = pd.read_csv(f"./results/{language}_probing.csv")
    for task in tasks:
        num_rows = len(df1.index)
        my_column_values = df1[task].tolist()
        # my_column_values = [eval(i) for i in my_column_values]

        multi = my_column_values[0:12]
        dict = {"score":multi}
        df = pd.DataFrame(dict)
        df.to_csv(f"./results/multi_{language}_{task}.csv")

        indic = my_column_values[12:24]
        dict = {"score":indic}
        df = pd.DataFrame(dict)
        df.to_csv(f"./results/indic_{language}_{task}.csv")

        xlm = my_column_values[24:36]
        dict = {"score":xlm}
        df = pd.DataFrame(dict)
        df.to_csv(f"./results/xlm_{language}_{task}.csv")

        muril = my_column_values[36:]
        dict = {"score":muril}
        df = pd.DataFrame(dict)
        df.to_csv(f"./results/muril_{language}_{task}.csv")
        
        

