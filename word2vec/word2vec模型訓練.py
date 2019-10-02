#!/usr/bin/env python
# coding: utf-8

# In[18]:


# -*- coding: utf-8 -*-

import logging
#import word2vec
from gensim.models import word2vec

def main():

    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    sentences = word2vec.LineSentence("test2_seg.txt")
    model=word2vec.Word2Vec(sentences,sg=1,min_count=1 ,size=300)
    #word2vec.word2vec('wiki_seg.txt', 'corpusWord2Vec.bin', size=300,verbose=True)
    
    #保存模型，供日後使用
    #model.save("word2vec.bin")
    model.save("word2vec2.model")

    #模型讀取方式
    # model = word2vec.Word2Vec.load("your_model_name")

if __name__ == "__main__":
    main()


# In[ ]:




