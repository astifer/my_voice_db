import hdbscan
import umap.umap_ as umap  # pip install umap-learn


def generate_clusters(
    message_embeddings, n_neighbors, n_components, min_cluster_size, random_state=None
):
    """
    Generate HDBSCAN cluster object after reducing embedding dimensionality with UMAP
    """

    umap_embeddings = umap.UMAP(
        n_neighbors=n_neighbors,
        n_components=n_components,
        metric="cosine",
        random_state=random_state,
    ).fit_transform(message_embeddings)

    clusters = hdbscan.HDBSCAN(
        min_cluster_size=min_cluster_size,
        metric="euclidean",
        cluster_selection_method="eom",
    ).fit(umap_embeddings)

    return clusters


def score_clusters(clusters, prob_threshold=0.05):
    """
    Returns the label count and cost of a given cluster supplied from running hdbscan
    """

    cluster_labels = clusters.labels_
    label_count = len(np.unique(cluster_labels))
    total_num = len(clusters.labels_)
    cost = np.count_nonzero(clusters.probabilities_ < prob_threshold) / total_num

    return label_count, cost
