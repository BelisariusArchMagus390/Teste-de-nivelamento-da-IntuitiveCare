import pytest
import requests
from unittest.mock import Mock
from test_1_web_scraping.web_scraping_pdf import DownloadPDFFile
from pathlib import Path

page_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

@pytest.fixture
def download_pdf_file():
    return DownloadPDFFile(page_url)

# tests of request_html()
def test_request_html_sucess(download_pdf_file, mocker):
    # create mock
    mock_response = Mock()
    mock_response.status_code = 200
    # simulate a response
    mock_response.text = """
    <html>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """ 
    # replace the response
    mocker.patch("requests.get", return_value=mock_response)
    mocker.patch.object(download_pdf_file, "page_url", page_url)

    response_function = download_pdf_file.request_html()

    assert response_function == True

def test_request_html_404_failure(download_pdf_file, mocker):
    # create mock
    mock_response = Mock()
    mock_response.status_code = 404
    # simulate a error 404 response
    mock_response.text = """
    <html>
        <body>
            <h1>Error 404</h1>
        </body>
    </html>
    """ 
    # replace the response
    mocker.patch("requests.get", return_value=mock_response)
    mocker.patch.object(download_pdf_file, "page_url", page_url)

    response_function = download_pdf_file.request_html()

    assert response_function == False

def test_request_html_timeout_failure(download_pdf_file, mocker):
    # create mock and simulate a timeout
    mock_response = Mock(side_effect=requests.exceptions.Timeout)
    # replace the response
    mocker.patch("requests.get", return_value=mock_response)
    mocker.patch.object(download_pdf_file, "page_url", page_url)

    response_function = download_pdf_file.request_html()

    assert response_function == False

# tests of search_pdf()
def test_search_pdf_sucess(download_pdf_file, mocker):
    # create mock
    mock_response = Mock()
    mock_response.status_code = 200
    # simulate a response
    mock_response.text = """
    <html>
        <body>
            <a href="http://gov.br/anexo.pdf">Anexo</a>
        </body>
    </html>
    """ 
    # replace the response
    mocker.patch.object(download_pdf_file, "request_html", return_value=True)
    mocker.patch.object(download_pdf_file, "request_response", mock_response)

    response_function = download_pdf_file.search_pdf("a", "Anexo")

    assert response_function == "http://gov.br/anexo.pdf"

def test_search_pdf_failure(download_pdf_file, mocker):
    # create mock
    mock_response = Mock()
    mock_response.status_code = 200
    # simulate a response
    mock_response.text = """
    <html>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """ 
    # replace the response
    mocker.patch.object(download_pdf_file, "request_html", return_value=False)
    mocker.patch.object(download_pdf_file, "request_response", None)

    response_function = download_pdf_file.search_pdf("a", "Anexo")

    assert response_function == None

# tests of download_pdf()
def test_download_pdf_sucess(download_pdf_file, mocker, tmp_path):
    pdf_content = b"%PDF-1.4 Tabela do anexo"

    # create mock
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "application/pdf"}
    mock_response.content = pdf_content

    # replace the response
    mocker.patch("requests.get", return_value=mock_response)
    # temporary directory path
    download_pdf_file.files_directory_path = tmp_path

    download_file = download_pdf_file.download_pdf("http://gov.br/anexo.pdf")

    # make verification of the request
    assert download_file is not None
    assert download_file.exists()
    # make verification if the content is the expected
    assert download_file.read_bytes() == pdf_content
    # remove the temporary file
    download_file.unlink()

def test_download_pdf_404_failure(download_pdf_file, mocker):
    # create mock
    mock_response = Mock()
    mock_response.status_code = 404

    # replace the response
    mocker.patch("requests.get", return_value=mock_response)

    download_file = download_pdf_file.download_pdf("http://gov.br/anexo.pdf")

    # make verification if the file exists
    assert download_file == None

def test_download_pdf_timeout_failure(download_pdf_file, mocker):
    # create mock
    mock_response = Mock(side_effect=requests.exceptions.Timeout)

    # replace the response
    mocker.patch("requests.get", return_value=mock_response)

    download_file = download_pdf_file.download_pdf("http://gov.br/anexo.pdf")

    # make verification if the file exists
    assert download_file == None

def test_download_type_file_invalid(download_pdf_file, mocker, tmp_path):

    # create mock
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.headers = {"Content-type": "text/html"}
    mock_response.content = b"""
    <html>
        <body>
            <h1>Hello World</h1>
        </body>
    </html>
    """ 

    # replace the response
    mocker.patch("requests.get", return_value=mock_response)
    # temporary directory path
    download_pdf_file.files_directory_path = tmp_path

    download_file = download_pdf_file.download_pdf("http://gov.br/anexo.pdf")

    assert download_file == None
    
def test_download_not_exists_directory(download_pdf_file, tmp_path):
    # create a temporary directory path
    downloaded_files_path_tmp = tmp_path.joinpath(tmp_path, "downloaded_files")
    # define the value of the atribute files_directory_path
    download_pdf_file.files_directory_path = downloaded_files_path_tmp

    # verify if the directory not exists
    assert not downloaded_files_path_tmp.exists()
    # create the directory if no exists
    download_pdf_file.files_directory_path.mkdir(parents=True, exist_ok=True)
    # verify if now the directory exists
    assert downloaded_files_path_tmp.exists()

# tests of compact_file()
def test_compact_file_sucess(download_pdf_file, tmp_path):
    download_pdf_file.files_directory_path = tmp_path

    zip_file = download_pdf_file.compact_file("pdf_files.zip")

    # make verification if the file exists
    assert zip_file is not None
    assert zip_file.exists()
    # remove the temporary file
    zip_file.unlink()

def test_compact_file_path_missing_failure(download_pdf_file, tmp_path):
    download_pdf_file.files_directory_path = None

    zip_file = download_pdf_file.compact_file("pdf_files.zip")

    # make verification if the file not exists
    assert zip_file == None