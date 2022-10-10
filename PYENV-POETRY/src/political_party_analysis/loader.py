from pathlib import Path
from typing import List
from urllib.request import urlretrieve
from sklearn.preprocessing import StandardScaler

import pandas as pd


class DataLoader:
    """Class to load the political parties dataset"""

    data_url: str = "https://www.chesdata.eu/s/CHES2019V3.dta"

    def __init__(self):
        self.party_data = self._download_data()
        self.non_features = []
        self.index = ["party_id", "party", "country"]

    def _download_data(self) -> pd.DataFrame:
        data_path, _ = urlretrieve(
            self.data_url,
            Path(__file__).parents[2].joinpath(*["data", "CHES2019V3.dta"]),
        )
        return pd.read_stata(data_path)

    def remove_duplicates(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.drop_duplicates()
        ##### YOUR CODE GOES HERE #####
        return df

    def remove_nonfeature_cols(self, df: pd.DataFrame, non_features: List[str], index: List[str]) -> pd.DataFrame:
        df = df.drop(non_features, axis =1)
        df = df.set_index(index)
        """Write a function to remove certain features cols and set certain cols as indices
        in a dataframe"""
        ##### YOUR CODE GOES HERE #####
        #pass
        return(df)

    def handle_NaN_values(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to handle NaN values in a dataframe"""
        df = df.fillna(1)
        #pass
        return (df)
    
    def scale_features(self, df: pd.DataFrame) -> pd.DataFrame:
        """Write a function to normalise values in a dataframe. Use StandardScaler."""
        scaler = StandardScaler()
        scaled_df = scaler.fit_transform(df)
        ##### YOUR CODE GOES HERE #####
        #pass
        return(scaled_df)


    def preprocess_data(self):
        """Write a function to combine all pre-processing steps for the dataset"""
        ##### YOUR CODE GOES HERE #####
        
        df = self.remove_duplicates(self.party_data)
        df = self.remove_nonfeature_cols(df, [], [])
        df = self.handle_NaN_values(df)
        df = self.scale_features(df)
        #print (df.head())
        return (df)

    

# DL = DataLoader()
# df = DL.remove_duplicates(DL.party_data)
# df = DL.remove_nonfeature_cols(df, ['eu_googov_require', 'eu_econ_require'], ['country', 'party'])
# df = DL.handle_NaN_values(df)
# df = DL.scale_features(df)
# print (df.head())

