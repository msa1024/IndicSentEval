"""Convert NER data from SSF to CoNLL format."""
from argparse import ArgumentParser
from re import search
import ssfAPI as ssf
import os


def read_lines_from_file(file_path):
    """Read lines from a file."""
    with open(file_path, 'r', encoding='utf-8') as file_read:
        return [line.strip() for line in file_read.readlines() if line.strip()]


def find_file_list(folder_path):
    """Find file list inside a folder."""
    file_list = ssf.folderWalk(folder_path)
    return file_list

def convert_into_conll_format(lines,sentence_count):
    """Convert lines into conll format."""
    conll_lines = []
    ner_flag = False
    ner_tag = ''
    ner_tokens = []
    nested_level = 0
    for line in lines:
        line_split = line.split('\t')
        if search('^\<Sentence', line):
            sentence_count += 1
        elif len(line_split) == 2:
            addr, token = line_split
            if not ner_flag:
                conll_lines.append(str(sentence_count) + '\t' + token + '\tO')
            else:
                ner_tokens.append(token)
        elif not ner_flag and len(line_split) == 4 and search('^\<ne=(.*?)\>', line_split[3]):
            ner_flag = True
            ner_tag = search('^\<ne=(.*?)\>', line_split[3]).group(1)
        elif ner_flag and len(line_split) == 4 and search('^\<ne=(.*?)\>', line_split[3]):
            nested_level += 1
        elif ner_flag and line == '))' and nested_level > 0: 
            nested_level -= 1
        elif ner_flag and line == '))' and nested_level == 0:
            ner_tokens_with_tags_and_sent_info = [str(sentence_count) + '\t' + tok + '\tB-' + ner_tag if index == 0 else str(sentence_count) + '\t' + tok + '\tI-' + ner_tag for index, tok in enumerate(ner_tokens)]
            conll_lines += ner_tokens_with_tags_and_sent_info
            ner_flag = False
            ner_tag = ''
            ner_tokens = []
        elif search('^\<\/Sentence\>', line):
            conll_lines.append('')
    return conll_lines,sentence_count


def write_lines_to_file(lines, file_path):
    """Write lines to a file."""
    with open(file_path, 'w', encoding='utf-8') as file_write:
        file_write.write('\n'.join(lines))


def main():
    """Pass arguments and call functions here."""
    parser = ArgumentParser()
    parser.add_argument('--input', dest='inp', help='Enter the input file path')
    parser.add_argument('--output', dest='out', help='Enter the output file path')
    args = parser.parse_args()


    if not os.path.isdir(args.inp):
        sentence_count = 0
        input_lines = read_lines_from_file(args.inp)
        conll_lines,c = convert_into_conll_format(input_lines,sentence_count)
        print(len(conll_lines))
        print(type(conll_lines))
        write_lines_to_file(conll_lines, args.out)
    else:
        file_list = find_file_list(args.inp)
        sentence_count = 0
        final_lines = []
        for file in file_list:
            input_lines = read_lines_from_file(file)
            conll_lines,sentence_count = convert_into_conll_format(input_lines,sentence_count)
            final_lines = final_lines+conll_lines
        write_lines_to_file(final_lines, args.out)


if __name__ == '__main__':
    main()
