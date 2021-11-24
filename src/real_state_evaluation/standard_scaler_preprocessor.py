from pandas import DataFrame
from real_state_evaluation.base import Preprocessor
from sklearn.preprocessing import StandardScaler


class StandardScalerPreprocessor(Preprocessor):

    def preprocess(self, train_df: DataFrame, test_df: DataFrame) -> (DataFrame, DataFrame):
        scaler = StandardScaler()
        scaler.fit(train_df[self.feature_names])

        preprocessed_train_df = self._transform(scaler, train_df)
        preprocessed_test_df = self._transform(scaler, test_df)
        return preprocessed_train_df, preprocessed_test_df

    def _transform(self, scaler, df):
        df_transformed = df.copy()
        df_transformed.loc[:, self.feature_names] = scaler.transform(df_transformed[self.feature_names])
        return df_transformed
