from data_summariser import __version__
import pytest
import pandas as pd
from data_summariser import summariser


def test_version():
    assert __version__ == '0.1.0'

data_summariser = None

@pytest.fixture
def setup_summariser():
	dd = {"a":[12,35,67], "b":[89, None, 90.5]}
	dataset = pd.DataFrame(dd)
	data_summariser = summariser.Summariser(dataset)
	return data_summariser


def test_is_dataframe(setup_summariser):
	assert setup_summariser.is_dataframe()


def test_get_type_frequencies(setup_summariser):
	type_series = list(setup_summariser.get_type_frequencies().to_dict().values())
	assert type_series == [1, 1]

def test_get_col_null_counts(setup_summariser):
	col_null_counts = list(setup_summariser.get_col_null_counts().values())
	assert col_null_counts == [0, 1]