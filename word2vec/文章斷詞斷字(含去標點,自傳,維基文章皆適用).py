#!/usr/bin/env python
# coding: utf-8

# In[1]:


# -*- coding: utf-8 -*-

import jieba
import logging

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

    # jieba custom setting.
    jieba.set_dictionary('jieba_dict/dict.txt.big')

    # load stopwords set
    stopword_set = set()
    with open('jieba_dict/stop_words.txt','r', encoding='utf-8') as stopwords:
        for stopword in stopwords:
            stopword_set.add(stopword.strip('\n'))

    output = open('test2_seg.txt', 'w', encoding='utf-8')
    with open('test2.txt', 'r', encoding='utf-8') as content :
        for texts_num, line in enumerate(content):
            line = line.strip('\n')
            line=line.replace('\n', '').replace('/', '').replace('(', '').replace(')', '').replace(']', '').replace('[', '').replace('.', '').replace('\n', '').replace(' ', '').replace(u'\u3000',u'').replace('，', '').replace('。', '').replace('？', '').replace('！', '').replace('“', '').replace('”', '').replace('：', '').replace('…', '').replace('（', '').replace('）', '').replace('—', '').replace('《', '').replace('》', '').replace('、', '').replace('‘', '').replace('’', '').replace('「', '').replace('」', '').replace('◎', '').replace(u'\xa0', u'').replace('．', '')
            line=str(line)
            words = jieba.cut(line, cut_all=False)
            for word in words:
                #if word.isdigit()==True:
                    #word=word.remove(item)
                if word not in stopword_set:
                    if word.isdigit()==False:
                        output.write(word + ' ')
            output.write('\n')

            if (texts_num + 1) % 10000 == 0:
                logging.info("已完成前 %d 行的斷詞" % (texts_num + 1))
    output.close()

if __name__ == '__main__':
    main()


# In[ ]:





# In[ ]:




