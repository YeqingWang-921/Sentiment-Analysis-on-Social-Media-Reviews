import os
import re
from bs4 import BeautifulSoup
import nltk
#import enchant
#from enchant.checker import SpellChecker
#nltk.download()

if __name__=='__main__':
    path = 'F:\\aclImdb_v1\\aclImdb'

    # read stopwords
    stopWords= []
    spfilename = 'stopwords.txt'
    with open(path + '\\' + spfilename, encoding='utf-8') as f:
        line = f.readline()
        print('start read stopwords')
        while line:
            # while line is not null
            stopWords.append(line[:-1])
            # [:-1] reserve \n of every line in stop words
            line = f.readline()
            # remove repeat stop words
        stopWords = set(stopWords)
        print('read done')


    # remove stopwords
    #d = enchant.Dict("en_US")
    testpath = 'F:\\aclImdb_v1\\IMDB\\pos\\check_pos.txt'
    raw_word_list = []
    sent_list = []
    #raw_file = 'test\\test.txt'
    with open(testpath, encoding='utf-8') as f:
        line = f.readline()
        while line:
            while '\n' in line:
                line = line.replace('\n', '')
            #remove punctuations and number
            if re.findall(u'[!\d"#$%&\'()*+,./:;<=>?@^_`{|}~]', line):
                tmp = re.findall(u'[!\d"#$%&\'()*+,./:;<=>?@^_`{|}~]', line)
                for i in tmp:
                    line = line.replace(i,'')

            if len(line) > 0:
                sentence = str(line)
                print(sentence)
                raw_word_list = list(nltk.word_tokenize(sentence))
                dealed_words = []
                for raw_word in raw_word_list:
                    word = str(raw_word)
                    stra = 'and'
                    strt = 'too'
                    #print('original word: ', word)

                    #print(word)'''word not in stopWords and'''
                    if word not in stopWords and ( word != stra ) and ( word != strt ):
                        #if (d.check(word)):
                        #print('dealed word: ', word.lower())
                        #raw_word_list.append(word)
                        #change the word in lower case to reduce redundency
                        lower_word = word.lower()
                        dealed_words.append(lower_word)
                sent_list.append(dealed_words)
            line = f.readline()

    #write file

    write_file = 'F:\\aclImdb_v1\\IMDB\\pos\\new_pos_check.txt'
    file = open(write_file, 'w', encoding='utf-8')
    for sent in sent_list:
        for i in range(len(sent)):
            s = sent[i] + ' '
            file.write(s)
        file.write('\n')


    print('have done!')
    file.close()


