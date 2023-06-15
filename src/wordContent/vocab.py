import ssfAPI as ssf
from argparse import ArgumentParser
from re import search
from sys import argv
import os
import pandas as pd

def find_file_list(folder_path):
    """Find file list inside a folder."""
    file_list = ssf.folderWalk(folder_path)
    return file_list


def extract_raw_sentences(file_path):
    """Extract raw sentences from a dependency annotated file."""
    ssf_document = ssf.Document(file_path)
    raw_sentences = []
    for sentence in ssf_document.nodeList:
        raw_sentences.append(sentence.generateSentence())
    return raw_sentences


def getTotalCorpus(inp):
    sentences = []
    if not os.path.isdir(inp):
        raw_sentences = extract_raw_sentences(inp)
        for item in raw_sentences:
            sentences.append(item)

    else:
        # file_list = find_file_list(inp)
        file_list = ['../../data/Hindi/Data/DISEASE/mor-1051-1100-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-तपेदिक-pos-chunk-401-422-posn-name', '../../data/Hindi/Data/DISEASE/mor-2501-2550-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-1301-1350-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_4.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-2951-3000-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-301-350-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-801-850-posn-name', '../../data/Hindi/Data/DISEASE/mor-2451-2500-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_1.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-निमोनिया-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-101-150-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-451-500-posn-name', '../../data/Hindi/Data/DISEASE/mor-2901-2950-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-तपेदिक-pos-chunk-201-250-posn-name', '../../data/Hindi/Data/DISEASE/domain-box-office-hindi-raw-sentences-550-utf_1.utf8.cml.V.tkn.cml_updated.mo.po', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment_pos_chunk-pos-chunk-601-650-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-851-900-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_entertainment_set16.txt-pos-chunk-401-450-posn-name', '../../data/Hindi/Data/DISEASE/mor-2751-2800-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_9.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/file-mouth_ka_saudagar-1507111034.dat', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_8.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-101-150-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment_pos_chunk-pos-chunk-51-100-posn-name', '../../data/Hindi/Data/DISEASE/mor-डिप्थीरिया-pos-chunk-51-72-posn-name', '../../data/Hindi/Data/DISEASE/domain-box-office-hindi-raw-sentences-550-utf_2.utf8.cml.V.tkn.cml_updated.mo.po', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_5.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-1501-1550-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-251-300-posn-name', '../../data/Hindi/Data/DISEASE/mor-2851-2900-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-401-450-posn-name', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_8.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_2.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-901-950-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-2301-2350-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-खसरा-pos-chunk-101-124-posn-name', '../../data/Hindi/Data/DISEASE/mor-ऑस्टियोपोरोसिस-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment-pos-chunk-701-750-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-651-700-posn-name', '../../data/Hindi/Data/DISEASE/mor-मलेरिया-1-50-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment_pos_chunk-pos-chunk-901-950-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set16-pos-chunk-151-200-posn-name', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_4.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/file-yes-sir-0707111505.dat', '../../data/Hindi/Data/DISEASE/domain-box-office-hindi-raw-sentences-550-utf_7.utf8.cml.V.tkn.cml_updated.mo.po', '../../data/Hindi/Data/DISEASE/domain-box-office-hindi-raw-sentences-550-utf_6.utf8.cml.V.tkn.cml_updated.mo.po', '../../data/Hindi/Data/DISEASE/mor-डिप्थीरिया-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-351-400-posn-name', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_6.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-1201-1250-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-2701-2750-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-2651-2700-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_1.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-101-150-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-501-550-posn-name', '../../data/Hindi/Data/DISEASE/mor-मलेरिया-101-150-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment_pos_chunk-pos-chunk-101-150-posn-name', '../../data/Hindi/Data/DISEASE/mor-2201-2250-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-1101-1150-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment-pos-chunk-951-1000-posn-name', '../../data/Hindi/Data/DISEASE/mor-751-800-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-धूम्रपान-pos-chunk-201-260-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment-pos-chunk-351-400-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment-pos-chunk-251-300-posn-name', '../../data/Hindi/Data/DISEASE/mor-351-400-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-2001-2050-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-901-950-posn-name', '../../data/Hindi/Data/DISEASE/mor-तपेदिक-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_7.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/file-khadi_ka_kurtha-0807112238.dat', '../../data/Hindi/Data/DISEASE/mor-धूम्रपान-pos-chunk-151-200-posn-name', '../../data/Hindi/Data/DISEASE/mor-ऑस्टियोपोरोसिस-pos-chunk-101-150-posn-name', '../../data/Hindi/Data/DISEASE/mor-1-50-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-551-600-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-ऑस्टियोपोरोसिस-pos-chunk-151-203-posn-name', '../../data/Hindi/Data/DISEASE/mor-तपेदिक-pos-chunk-101-150-posn-name', '../../data/Hindi/Data/DISEASE/mor-2551-2600-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-951-1000-posn-name', '../../data/Hindi/Data/DISEASE/mor-2601-2650-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_2.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-निमोनिया-pos-chunk-101-150-posn-name', '../../data/Hindi/Data/DISEASE/mor-2401-2450-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_10.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-501-550-posn-name', '../../data/Hindi/Data/DISEASE/file-kiraye_ka_ghar-1507111043.dat', '../../data/Hindi/Data/DISEASE/file-doli_banaam_arthi.dat', '../../data/Hindi/Data/DISEASE/mor-1251-1300-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-मलेरिया-pos-chunk-51-100-posn-name', '../../data/Hindi/Data/DISEASE/mor-801-850-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-1851-1900-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_6.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-1801-1850-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-2801-2850-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_6.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-1601-1650-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-201-250-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-401-450-posn-name', '../../data/Hindi/Data/DISEASE/mor-मलेरिया-151-204-posn-name', '../../data/Hindi/Data/DISEASE/mor-खसरा-pos-chunk-51-100-posn-name', '../../data/Hindi/Data/DISEASE/mor-तपेदिक-pos-chunk-151-200-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set16-pos-chunk-51-100-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/mor-निमोनिया-pos-chunk-151-200-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-901-950-posn-name', '../../data/Hindi/Data/DISEASE/mor-पार्किंसन-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-551-600-posn-name', '../../data/Hindi/Data/DISEASE/mor-1401-1450-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-251-300-posn-name', '../../data/Hindi/Data/DISEASE/domain-box-office-hindi-raw-sentences-550-utf_10.utf8.cml.V.tkn.cml_updated.mo.p', '../../data/Hindi/Data/DISEASE/mor-hin_entertainment_set16.txt-pos-chunk-301-350-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-351-400-posn-name', '../../data/Hindi/Data/DISEASE/file-katl_e_bayan-1507111042.dat', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-151-200-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-601-650-posn-name', '../../data/Hindi/Data/DISEASE/mor-851-900-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-51-100-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-651-700-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set16-pos-chunk-251-300-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment_pos_chunk-pos-chunk-151-200-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-51-100-posn-name', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_5.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-धूम्रपान-pos-chunk-101-150-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment-pos-chunk-551-600-posn-name', '../../data/Hindi/Data/DISEASE/file-parithyaag-0707111503.dat', '../../data/Hindi/Data/DISEASE/mor-डेंगू-pos-chunk-51-100-posn-name', '../../data/Hindi/Data/DISEASE/domain-box-office-hindi-raw-sentences-550-utf_5.utf8.cml.V.tkn.cml_updated.mo.po', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_11.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/file-andhe_ki_lathi-1507111038.dat', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_9.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/file-udhaar-0707111504.dat', '../../data/Hindi/Data/DISEASE/mor-2351-2400-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-खसरा-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/mor-201-250-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-पार्किंसन-pos-chunk-51-74-posn-name', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_7.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_4.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_7.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-501-550-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-2101-2150-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-401-450-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment_pos_chunk-pos-chunk-751-800-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-201-250-posn-name', '../../data/Hindi/Data/DISEASE/mor-1151-1200-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-1551-1600-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-1951-2000-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/mor-1451-1500-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-1751-1800-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-धूम्रपान-pos-chunk-51-100-posn-name', '../../data/Hindi/Data/DISEASE/mor-1001-1050-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_3.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set16-pos-chunk-451-500-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-701-750-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment_pos_chunk-pos-chunk-851-900-posn-name', '../../data/Hindi/Data/DISEASE/mor-निमोनिया-pos-chunk-201-237-posn-name', '../../data/Hindi/Data/DISEASE/mor-451-500-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_5.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment_pos_chunk-651-700-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_entertainment_set16.txt-pos-chunk-551-600-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-451-500-posn-name', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_9.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment-pos-chunk-301-350-posn-name', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_10.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-251-300-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/mor-151-200-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-डेंगू-pos-chunk-151-200-posn-name', '../../data/Hindi/Data/DISEASE/mor-निमोनिया-pos-chunk-51-100-posn-name', '../../data/Hindi/Data/DISEASE/mor-1351-1400-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-951-1000-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment-pos-chunk-501-550-posn-name', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_3.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-1701-1750-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-701-750-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-डेंगू-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/mor-651-700-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-धूम्रपान-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_8.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-2251-2300-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment_pos_chunk-pos-chunk-801-850-posn-name', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_2.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-851-900-posn-name', '../../data/Hindi/Data/DISEASE/file-tyaag-1507111040.dat', '../../data/Hindi/Data/DISEASE/domain-box-office-hindi-raw-sentences-550-utf_4.utf8.cml.V.tkn.cml_updated.mo.po', '../../data/Hindi/Data/DISEASE/domain-box-office-hindi-raw-sentences-550-utf_9.utf8.cml.V.tkn.cml_updated.mo.po', '../../data/Hindi/Data/DISEASE/mor-इनफ्लुएंजा-pos-chunk-51-69-posn-name', '../../data/Hindi/Data/DISEASE/mor-डेंगू-pos-chunk-251-270-posn-name', '../../data/Hindi/Data/DISEASE/file-sapna-0707111503.dat', '../../data/Hindi/Data/DISEASE/mor-1901-1950-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-1651-1700-posn-name.txt', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_3.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-601-650-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-151-200-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-51-100-posn-name', '../../data/Hindi/Data/DISEASE/file-rishthey_ka_dhaag-0807112232.dat', '../../data/Hindi/Data/DISEASE/mor-तपेदिक-pos-chunk-351-400-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-301-350-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-751-800-posn-name', '../../data/Hindi/Data/DISEASE/mor-hindi_set21_entertainment_pos_chunk-pos-chunk-201-250-posn-name', '../../data/Hindi/Data/DISEASE/domain-box-office-hindi-raw-sentences-550-utf_3.utf8.cml.V.tkn.cml_updated.mo.po', '../../data/Hindi/Data/DISEASE/domain-box-office-hindi-raw-sentences-550-utf_8.utf8.cml.V.tkn.cml_updated.mo.po', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set1-pos-chunk-551-600-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-701-750-posn-name', '../../data/Hindi/Data/DISEASE/mor-hin_agriculture_set6-pos-chunk-1001-1014-posn-name', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_11.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-इनफ्लुएंजा-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/domain-gadget-hindi-raw-sentences-550-utf_10.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-2051-2100-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hindi_entertainment_set16-pos-chunk-201-250-posn-name', '../../data/Hindi/Data/DISEASE/mor-पोलियो-pos-chunk-1-50-posn-name', '../../data/Hindi/Data/DISEASE/domain-cricket-hindi-raw-sentences-550-utf_1.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-2151-2200-posn-name.txt', '../../data/Hindi/Data/DISEASE/mor-hin_entertainment_set16.txt-pos-chunk-501-550-posn-name', '../../data/Hindi/Data/DISEASE/mor-तपेदिक-pos-chunk-251-300-posn-name', '../../data/Hindi/Data/DISEASE/domain-recipe-hindi-raw-sentences-550-utf_11.utf8.cml.V.tkn.cml_updated.mo.pos.chnk', '../../data/Hindi/Data/DISEASE/mor-डेंगू-pos-chunk-101-150-posn-name', '../../data/Hindi/Data/DISEASE/mor-डेंगू-pos-chunk-201-250-posn-name']
        for fl in file_list:
            raw_sentences = extract_raw_sentences(fl)
            for item in raw_sentences:
                sentences.append(item)

    
    return sentences

def write_lines_to_file(lines, file_path):
    with open(file_path, 'w', encoding='utf-8') as file_write:
        file_write.write('\n'.join(lines))

def main():

    parser = ArgumentParser(description="This is a program for extracting raw sentences from dependency annotated treebanks.")
    parser.add_argument('-i', dest='inp')
    parser.add_argument('-o',dest='out')
    args = parser.parse_args()

    wordContent = []
    sent = []
    index = []

    sentences = getTotalCorpus(args.inp)
    vocabulary = {}
    data = ""

    for item in sentences:
        data += item
        data += " "
    data = data.split(" ")
    vocab = []
    for sentence in sentences:
        for item in sentence.split(" "):
            vocab.append(item)
    vocab = list(set(vocab))
    with open(args.out, "w") as f:
        f.write(str(vocab))
    exit(0)
    with open("vocab.txt", "w") as f:
        for item in vocab:
            f.write(item)
            f.write("\t")
            f.write(str(data.count(item)))
            vocabulary.update({item:data.count(item)})
            f.write("\n")
        f.close()
    vocabulary = dict(sorted(vocabulary.items(), key=lambda item: item[1]))

    sampled_words = []
    for item in vocabulary.keys():
        if vocabulary[item] > 25 and vocabulary[item] < 100:
            sampled_words.append(item)

    for word in sampled_words:
        count  = 0
        indx = 0
        for i in range(len(sentences)):
            sentence = sentences[i]
            x = sentence.split(" ")
            if word in x and count <= 5:
                count += 1
                wordContent.append(word)
                sent.append(sentence)
                index.append(i)

    
    # write_lines_to_file(wordContent, "wordContent.txt")
    d = {"WordContent":wordContent,"sentences":sent,"index":index}
    df = pd.DataFrame(d)
    df.to_csv(args.out,index=False)


if __name__ == '__main__':
    main()
