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

# tests of get_table()
def test_get_table_pdf_valido(mocker, data_transformation):
    mocker.patch.object(data_transformation, "get_path", return_value="test.pdf")
    mock_read_pdf = mocker.patch("data_transformation.tabula.read_pdf")
    
    mock_read_pdf.return_value = [pd.DataFrame({"col1": [1, 2], "col2": [3, 4]})]

    result = data_transformation.get_table("test.pdf")

    assert result is True
    assert data_transformation.tables_dataframe is not None
    assert isinstance(data_transformation.tables_dataframe, pd.DataFrame)
    assert not data_transformation.tables_dataframe.empty
    mock_read_pdf.assert_called_once_with("test.pdf", pages="3-181", lattice=True, multiple_tables=True, encoding="latin1")