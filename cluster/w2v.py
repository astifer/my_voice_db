from gensim.models import Word2Vec
import numpy as np
import json

from create_all_data import all_json_to_df


def file_2_vectors(file) -> list:
    """

    :params file: json-file
    :return embeddings list:
    """
    answers = []
    with open(file, encoding='utf_8') as f:
        q_a = json.loads(f.read())
        q = q_a["question"]
        for a in q_a["answers"]:
            answers.append([a["answer"], q])

    corpus = []
    for sentence in answers:
        corpus.append(sentence[0].split())
    model = Word2Vec(corpus, vector_size=100, min_count=1)

    vectors = []
    for sentence in answers:
        if len(sentence[0]) == 0:
            word_vec = [0] * 100
        elif sentence[0] not in model.wv.key_to_index.keys():
            w_vs = []
            for word in sentence[0].split():
                w_vs.append(model.wv[word])
            word_vec = np.mean(np.array(w_vs), axis=0)
        else:
            word_vec = model.wv[sentence[0]]
        vectors.append(word_vec)

    return vectors

#if __name__ == "__main__":
    # print(file_2_vectors("data/1704.json"))
