# -*- coding:utf-8 -*-
import re
import sys
import nltk
import json
from wordcloud import WordCloud
from io import open
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


class GREText:
    def __init__(self, file_dir):
        self.file_dir = file_dir
        self.raw_text = self.get_text(self.file_dir)
        self.token = self.get_token()
        self.word_count = self.get_count()
        self.word_list = self.get_word()
        self.text = nltk.text.Text(self.token)

    #################### Data Process ##########################

    def get_text(self, file_dir):
        text = list()
        with open(file_dir, 'r') as f:
            text = f.read()
            text = text.lower()
            # remove symbols
            txt = re.sub(
                r'\n.\.\s|[0-9\.\!\/_,$%^*(\"\')\:]+|[-—–()?‘’“”【】";"！，。？、~@#￥%……&*（）]+', ' ', text)
            # remove i,ii,iii
            txt = re.sub(r'\si+\s', ' ', txt)
            # remove singal letter
            txt = re.sub(r'\s\S\s', ' ', txt)
            # remove multiple space
            txt = re.sub(r'\s+', ' ', txt)
        return txt

    def get_token(self, lemmatize=True):
        Stop_word = set(stopwords.words('english'))
        raw_word_token = nltk.word_tokenize(self.raw_text)
        token = [i for i in raw_word_token if i not in Stop_word]
        if lemmatize:
            lemmatizer = WordNetLemmatizer()
            token = [lemmatizer.lemmatize(i) for i in token]
        return token

    def get_count(self):
        fdist = nltk.FreqDist(self.token)
        return fdist

    def get_word(self):
        return self.word_count.keys()

    #################### Analysis Function ##########################

    def plot_freq(self, num=30):
        self.word_count.plot(num)

    def sort_word(self, reverse=False):
        return sorted(self.word_count.items(), key=lambda item: item[1], reverse=reverse)

    def lookup(self, wordstr):
        return self.word_count[wordstr]

    def concordance(self, wordstr):
        return self.text.concordance(wordstr)

    def common_contexts(self, wordstr1, wordstr2):
        return self.text.common_contexts(wordstr1, wordstr2)

    def collocations(self):
        return self.text.collocations()

    def word_cloud(self):
        wordcloud = WordCloud(background_color="white",width=1000,height=860,margin=2).generate(self.raw_text)
        plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis("off")
        plt.show()

    #################### Save ##########################

    def save_json(self, save_dir, format='dict'):
        if format == 'dict':
            with open(save_dir, 'w') as fs:
                json.dump(self.word_count, fs)
                print('Save Success.')
        if format == 'list':
            with open(save_dir, 'w') as fs:
                json.dump(self.sort_word(), fs)
                print('Save Success.')

    def save_txt(self, save_dir, format='list'):
        if format == 'list':
            with open(save_dir, 'w') as fs:
                for i in self.sort_word():
                    fs.write(str(i[0])+'\t'+str(i[1])+'\n')
                print('Save Success.')
