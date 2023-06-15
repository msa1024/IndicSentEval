import ssfAPI as ssf
from argparse import ArgumentParser
from re import search
from sys import argv
import os
import random
import pandas as pd


def getTotalCorpus(inp):
  sentences = []
  df = pd.read_csv(inp)
  temp = df["dropped"]
  return temp

def main():
    parser = ArgumentParser(description="This is a program for extracting raw sentences from dependency annotated treebanks.")
    parser.add_argument('-i', dest='inp')
    parser.add_argument('-o', dest='out')
    args = parser.parse_args()

    df = pd.read_csv("/home/aforakhilesh/iiit/research/IndicBertology/src/gold/hindi/bshift.csv")
    BShift = df["BShift"]
    shifted_sentences = []
    sentences = getTotalCorpus(args.inp)

    for i in range(len(sentences)):
        sentence = sentences[i]
        if(BShift[i]):
            sentence = sentence.split(" ")
            b = random.randint(0,len(sentence)-2)
            tmp = sentence[b]
            sentence[b] = sentence[b+1]
            sentence[b+1] = tmp
            sentence = " ".join(sentence)
            shifted_sentences.append(sentence)
        else:
            shifted_sentences.append(sentence)

    d = {"BShift":BShift,"sentences":shifted_sentences}
    df = pd.DataFrame(d)
    df.to_csv(args.out,index=False)

if __name__ == '__main__':
    main()
