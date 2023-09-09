from gensim.models import Word2Vec
import numpy as np
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

    for a in q_a['answers']:
        length_a = len(a['answer'])
        data_raw_all.append([a['answer'], q, length_a])
data_all = pd.DataFrame(data_raw_all,
                        columns=['answer', 'question', 'len_answer'])

corpus = []
for sentence in data_all[data_all['question'] == 'Что является главным «стоп»-фактором для запуска Новых бизнесов?']['answer'].items():
  corpus.append(sentence[1].split())

"""
сверху штуки для текста
"""

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