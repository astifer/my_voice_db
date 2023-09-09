from gensim.models import Word2Vec
import numpy as np

from create_all_data import all_json_to_df


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

    return vectors
