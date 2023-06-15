import pandas as pd
# read the text data
with open('results_telugu_xlm.txt', 'r') as f:
    text = f.read()

# extract the data and create a dataframe
columns = ['Sentence Length', 'Object Number', 'Subject Number', 'Tree Depth']
text = text.split("\n\n")
ultimate = [["*","*","*","*"],['Sentence Length', 'Object Number', 'Subject Number', 'Tree Depth']]
ultimate_pd = pd.DataFrame(ultimate,columns=columns)
count = 0    
for item in text:
    item = str(item)
    if count == 0:
        senlen = item.split("\n")
        count += 1
    elif count == 1:
        objnum = item.split("\n")
        count += 1
    elif count == 2:
        subnum = item.split("\n")
        count += 1
    elif count == 3:
        treedepth = item.split("\n")
        count = 0

        temp = []
        for i in range(12):
            t = []
            t.append(str(senlen[i]))
            t.append(str(objnum[i]))
            t.append(str(subnum[i]))
            t.append(str(treedepth[i]))
            temp.append(t)
        # print(len(temp[0]))
        df = pd.read_csv("data.csv")
        df_new = pd.DataFrame(temp,columns=columns)
        df_updated = pd.concat([df,df_new])
        df_updated_twice = pd.concat([df_updated,ultimate_pd])
        df_updated_twice.to_csv("data.csv",index=False)