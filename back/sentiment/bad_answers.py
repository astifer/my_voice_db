import nltk

# nltk.download("punkt")
import numpy as np
import pandas as pd
from nltk.tokenize import word_tokenize
from string import punctuation
from sklearn.model_selection import train_test_split

from catboost.core import CatBoostClassifier

import re

from pymystem3 import Mystem


model = CatBoostClassifier()
model.load_model("back/sentiment/models/model", format="cbm")


def text_cleaner(text):
    tokenized_text = word_tokenize(text, language="russian")
    clean_text = [
        word.lower()
        for word in tokenized_text
        if word not in punctuation and word != "\n"
    ]
    r = re.compile("[а-яА-Я]+")
    russian_text = " ".join([w for w in filter(r.match, clean_text)])
    return russian_text


def lemmatized(comments):
    lemmatizator = Mystem()
    text_for_lemmatization = " sep ".join(comments)

    lemmatizated_text = lemmatizator.lemmatize(text_for_lemmatization)
    lemmatizated_text_list = [
        word for word in lemmatizated_text if word != " " and word != "-"
    ]

    lemmatizated_text = " ".join(lemmatizated_text_list)
    lemmatizated_array = np.asarray(lemmatizated_text.split(" sep "))

    return lemmatizated_array


def set_bad_words():
    with open("back/sentiment/bad_words.txt", "r") as f:
        raw_words = f.readlines()

    b_w = []
    for i in range(len(raw_words)):
        if raw_words[i] == "\n":
            continue
        else:
            b_w.append(text_cleaner(raw_words[i]))
    bad_words = set(b_w)

    return bad_words


def is_any_bad(text):
    bad_words = set_bad_words()
    c = 0
    for a in text.split():
        if a in bad_words:
            c += 1
    return c


def bad_answers(df) -> pd.DataFrame:
    df["answer"] = df["answer"].apply(lambda x: text_cleaner(x))
    df = df.drop(df[df["answer"] == ""].index)

    comments = df["answer"].to_numpy()
    df["text"] = lemmatized(comments)  # 'верблюд то за что дебил бл'
    df["bad_words"] = df["text"].apply(is_any_bad)

    # нужно только text&bad_words
    X_test = df.drop(['answer','question'], axis=1)
    X_test['bad_words'] = df['bad_words']

    print(X_test)
    y_predict = model.predict(X_test)

    X_test["temp"] = np.ones(len(X_test))
    bad_data = X_test[X_test["temp"] * y_predict == 1]

    return bad_data
