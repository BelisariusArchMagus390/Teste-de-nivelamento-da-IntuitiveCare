import pytest
from test_2_data_transformation.data_transformation import DataTransformationPDFtoCSV
from unittest.mock import patch, MagicMock
import pandas as pd
from pathlib import Path

@pytest.fixture
def data_transformation():
    return DataTransformationPDFtoCSV()

# test of get_path()
def test_get_path_not_exists_directory(data_transformation, tmp_path):
    # create a temporary directory path
    data_files_path_tmp = tmp_path.joinpath(tmp_path, "data")
    # define the value of the atribute file_path
    data_transformation.file_path = data_files_path_tmp

    # verify if the directory not exists
    assert not data_files_path_tmp.exists()
    # create the directory if no exists
    data_transformation.file_path.mkdir(parents=True, exist_ok=True)
    # verify if now the directory exists
    assert data_files_path_tmp.exists()