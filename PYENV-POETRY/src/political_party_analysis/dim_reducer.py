from sklearn.decomposition import PCA
import pandas as pd


class DimensionalityReducer:
    """Class to model a dimensionality reduction method for the given dataset.
    1. Write a function to convert the high dimensional data to 2 dimensional.
    """

    def __init__(self, data: pd.DataFrame, n_components: int = 2):
        self.n_components = n_components
        self.data = data
        self.feature_columns = data.columns

    def apply_dim_reduction(data : pd.DataFrame, n_components: int = 2):
        pca = PCA(n_components=2)
        pca.fit(data)
        data_pca = pca.transform(data)
        data_pca = pd.DataFrame(data_pca, columns = ['PC1', 'PC2'])
        return (data_pca)

    ##### YOUR CODE GOES HERE #####
