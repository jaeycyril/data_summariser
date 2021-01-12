import numpy as np
import pandas as pd

class Summariser:
    
    def __init__(self, dataset: pd.core.frame.DataFrame):
    	if isinstance(dataset, pd.core.frame.DataFrame):
    		self.dataset = dataset
    	else:
    		raise Exception("Dataset is not a Pandas Dataset")

    def is_dataframe(self) -> bool:
    	return isinstance(self.dataset, pd.core.frame.DataFrame)

    def get_info(self) -> None:
        print(self.dataset.info())

    def get_type_frequencies(self) -> pd.core.series.Series:
    	return self.dataset.dtypes.value_counts()

    def get_col_null_counts(self):
    	cols = self.dataset.columns.tolist()
    	null_counter = {}

    	for col in cols:
    		null_counter[col] = self.dataset[col].isnull().sum()

    	return null_counter
