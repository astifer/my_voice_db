import pandas as pd

import umap.umap_ as umap # pip install umap-learn

from w2v import file_2_vectors
from generate_clusters import generate_clusters, score_clusters
from create_all_data import file_2_df


def clusters_2_df(
    embeddings, clusters, w2v_model, df_texts, n_neighbors=15, min_dist=0.1
) -> pd.DataFrame:
    """

    Arguments:
        embeddings: embeddings to use
        clusters: HDBSCAN object of clusters
        n_neighbors: float, UMAP hyperparameter n_neighbors
        min_dist: float, UMAP hyperparameter min_dist for effective
                  minimum distance between embedded points

    """
    umap_data = umap.UMAP(
        n_neighbors=n_neighbors,
        n_components=2,
        min_dist=min_dist,
        # metric='cosine',
        random_state=42,
    ).fit_transform(embeddings)

    texts = []
    for i in range(len(embeddings)):
        text = str(w2v_model.wv.most_similar(positive=embeddings[i], topn=1)[0][0])
        texts.append(
            [
                text[: len(text) - len(df_texts["question"][0])],
                umap_data[i][0],
                umap_data[i][1],
            ]
        )

    result = pd.DataFrame(texts, columns=["answer", "x", "y"])
    print(result)
    result["labels"] = clusters.labels_

    clustered = result[result.labels != -1]

    return clustered


if __name__ == "__main__":
    vectors, model = file_2_vectors("data/all/1036.json")
    data_json = file_2_df("data/all/1036.json")

    clusters_default = generate_clusters(
        vectors, n_neighbors=5, n_components=1, min_cluster_size=5, random_state=42
    )

    labels_def, cost_def = score_clusters(clusters_default)
    print(labels_def)
    print(cost_def)

    clustered_data = clusters_2_df(
        vectors, clusters_default, model, data_json, n_neighbors=5
    )
    print(clustered_data.head(5))
