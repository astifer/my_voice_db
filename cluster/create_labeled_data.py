import json
from os import listdir
from os.path import isfile, join
import pandas as pd

labeled_path = "labeled"
labeled_files = [f for f in listdir(labeled_path) if isfile(join(labeled_path, f))]

data_raw = []
for l_file in labeled_files:
    try:
        with open("labeled/" + l_file) as f:
            q_a = json.loads(f.read())
    except:
        continue
    q = q_a["question"]

    for a in q_a["answers"]:
        if a["sentiment"] == "negatives":
            sentiment = 0
        elif a["sentiment"] == "positives":
            sentiment = 2
        else:
            sentiment = 1

        if a["count"] > 1:
            for _ in range(int(a["counts"])):
                data_raw.append([a["answer"], q, a["sentiment"], a["cluster"], 1])
        else:
            data_raw.append([a["answer"], q, a["sentiment"], a["cluster"], a["count"]])

data = pd.DataFrame(
    data_raw, columns=["answer", "question", "sentiment", "cluster", "count"]
)
