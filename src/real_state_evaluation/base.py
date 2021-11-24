from abc import ABCMeta, abstractmethod
from typing import List

from pandas import DataFrame


class Preprocessor(metaclass=ABCMeta):
    def __init__(self, feature_names: List[str]):
        self.feature_names = feature_names

    @abstractmethod
    def preprocess(self, train_df: DataFrame, test_df: DataFrame) -> (DataFrame, DataFrame):
        return NotImplementedError
