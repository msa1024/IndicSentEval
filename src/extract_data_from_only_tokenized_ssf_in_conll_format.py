"""Extract data in conll format for tokenized data in SSF format."""
from argparse import ArgumentParser
from re import findall
from re import S


def read_text_from_file(file_path):
    '''
    Read text from a file.
    :param file_path: Path of the file.
    :return text: Text read from the file.
    '''
    with open(file_path, 'r', encoding='utf-8') as file_read:
        return file_read.read()


def find_sentences_from_ssf_text(text):
    '''
    Find sentences in SSF text.
    :param text: SSF text
    :return sentences: List of sentences enclosed under Sentence tag.
    '''
    text = text.replace('0xe0', '')
    sentence_pattern = "<Sentence id='?\"?.*?'?\"?>(.*?)</Sentence>"
    return findall(sentence_pattern, text, S)


def extract_data_in_conll_format(sentences):
    '''
    Extract data from sentences in SSF format into CoNLL format.
    :param sentences: Sentences in SSF format
    :return CoNLL_sentences: Sentences in CoNLL format.
    '''
    conll_sentences = list()
    for index, sentence in enumerate(sentences):
        temp_conll_sentence = list()
        for token in sentence.split('\n'):
            token = token.strip()
            if token:
                addr, token, pos = token.split('\t')[: 3]
                temp_conll_sentence.append(token)
        conll_sentences.append('\n'.join(temp_conll_sentence))
        conll_sentences.append('')
    return conll_sentences


def write_lines_to_file(lines, file_path):
    '''
    Write lines to a file.
    :param lines: Lines or list of texts to be written to a file.
    :param file_path: Path of the output file.
    :return: None
    '''
    with open(file_path, 'w', encoding='utf-8') as file_write:
        file_write.write('\n'.join(lines) + '\n')


def main():
    '''
    Pass arguments and call functions here.
    '''
    parser = ArgumentParser()
    parser.add_argument('-i', dest='inp', help='Enter input file path in SSF format.')
    parser.add_argument('-o', dest='out', help='Enter output file path which will written in CoNLL format.')
    args = parser.parse_args()
    input_text = read_text_from_file(args.inp)
    ssf_sentences = find_sentences_from_ssf_text(input_text)
    conll_sentences = extract_data_in_conll_format(ssf_sentences)
    write_lines_to_file(conll_sentences, args.out)


if __name__ == '__main__':
    main()