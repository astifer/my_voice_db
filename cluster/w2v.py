from gensim.models import Word2Vec
import numpy as np
import json
from os import listdir
from os.path import isfile, join
import pandas as pd

all_path = 'all'
all_files = [f for f in listdir(all_path) if isfile(join(all_path, f))]

data_raw_all = []
for a_file in all_files:
    try:
        with open("all/" + a_file) as f:
            q_a = json.loads(f.read())
    except:
        print(a_file)
        pass
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
for sentence in data_all[data_all['question'] == 'Что является главным «стоп»-фактором для запуска Новых бизнесов?']['answer']:
  if sentence not in model.wv.key_to_index.keys():
    print(sentence)
    w_vs = []
    for word in sentence.split():
      w_vs.append(model.wv[word])
    word_vec = np.mean(np.array(w_vs), axis=0)
  else:
    word_vec = model.wv[sentence]
  vectors.append(word_vec)
print(len(vectors))