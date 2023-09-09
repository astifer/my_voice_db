from gensim.models import Word2Vec
import numpy as np
<<<<<<< HEAD
import json
from os import listdir
from os.path import isfile, join
import pandas as pd
import logging

all_path = 'data/train_dataset_Мой голос/all/'
all_files = [f for f in listdir(all_path) if isfile(join(all_path, f))]

data_raw_all = []
c=0
for a_file in all_files:
    try:
        with open(all_path + a_file) as f:
            q_a = json.loads(f.read())
    except:
        logging.warning(a_file, c)
        c+=1
        continue
      
    q = q_a['question']
=======

from create_all_data import all_json_to_df

>>>>>>> origin/cluster

def file_2_vectors(file, question, corpus) -> list:
    """

    :params corpus:
            question:
            file:
    :return list:
    """
    data_all = all_json_to_df(file)
    model = Word2Vec(corpus, vector_size=100, min_count=1)

    vectors = []
    for sentence in data_all[data_all["question"] == question]["answer"]:
        if len(sentence) == 0:
            word_vec = [0] * 100
        elif sentence not in model.wv.key_to_index.keys():
            w_vs = []
            for word in sentence.split():
                w_vs.append(model.wv[word])
            word_vec = np.mean(np.array(w_vs), axis=0)
        else:
            word_vec = model.wv[sentence]
        vectors.append(word_vec)

<<<<<<< HEAD
model = Word2Vec(corpus, vector_size=100, min_count=1)
vectors = []
for word in corpus:
  # if word in model.wv.key_to_index.keys():
  word_vec = []
  for w in word:
    word_vec.append(model.wv.get_vector(w))
  vectors.append(word_vec)
  
  
def file_2_vectors(file)->list:
    
    return []
=======
    return vectors
>>>>>>> origin/cluster
