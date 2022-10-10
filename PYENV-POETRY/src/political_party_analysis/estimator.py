import pandas as pd
from pathlib import Path
from matplotlib import pyplot
from political_party_analysis.loader import DataLoader
from political_party_analysis import dim_reducer


class DensityEstimator:
    """Class to estimate Density/Distribution of the given data.
    1. Write a function to model the distribution of the political party dataset
    2. Write a function to randomly sample 10 parties from this distribution
    3. Map the randomly sampled 10 parties back to the original higher dimensional
    space as per the previously used dimensionality reduction technique.
    """

    def __init__(self, data: pd.DataFrame, dim_reducer, high_dim_feature_names):
        self.data = data
        self.dim_reducer_model = dim_reducer.model
        self.feature_names = high_dim_feature_names
        return
    
    def model_distribution(self, data: pd.DataFrame):
        pyplot.hist(data, bins=10)
        #pyplot.show()
        pyplot.savefig(Path(__file__).parents[1].joinpath(*["plots", "probability_distribution.png"]))

    ##### YOUR CODE GOES HERE #####

DL = DataLoader()
DE = DensityEstimator()
df = DL.preprocess_data()
print (df)
DE.model_distribution()