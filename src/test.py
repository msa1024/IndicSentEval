# from wxconv import WXC
# import collections

# con = WXC(order="wx2utf",lang="tel")

import pandas as pd

df = pd.read_csv("./CleanedTeluguTrain.csv")

# data = [tuple(x) for x in df.values]
# # print(data)

# sentences_dict = collections.defaultdict(list)
# for index, word,_ in data:
#     sentences_dict[index].append(word)

# sentences = [' '.join(words) for words in sentences_dict.values()]

# print(sentences)

for i in range(len(df)):
    df["word"][i] == str(df["word"][i])
    df["tag"][i] == str(df["tag"][i])

df.to_csv("CleanedTeluguTrain.csv")