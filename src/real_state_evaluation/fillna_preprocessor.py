from pandas import DataFrame
from real_state_evaluation.base import Preprocessor


class FillnaPreprocessor(Preprocessor):
    def __init__(self, feature_names, fill_value=0):
        super().__init__(feature_names)
        self.fill_value = fill_value

    def preprocess(self, train_df: DataFrame, test_df: DataFrame) -> (DataFrame, DataFrame):
        preprocessed_train_df = self._transform(train_df)
        preprocessed_test_df = self._transform(test_df)
        return preprocessed_train_df, preprocessed_test_df

    def _transform(self, df):
        df_transformed = df.copy()
        df_transformed.loc[:, self.feature_names] = df_transformed[self.feature_names].fillna(self.fill_value)
        return df_transformed
