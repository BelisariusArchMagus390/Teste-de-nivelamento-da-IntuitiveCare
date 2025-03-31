import pytest
import requests
from unittest.mock import Mock
from test_1_web_scraping.web_scraping_pdf import DownloadPDFFile;

page_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"

@pytest.fixture
def download_pdf_file():
    return DownloadPDFFile()

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

    assert download_pdf_file.request_html(page_url) == True

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

    assert download_pdf_file.request_html(page_url) == False

def test_request_html_timeout_failure(download_pdf_file, mocker):
    # create mock and simulate a timeout
    mock_response = Mock(side_effect=requests.exceptions.Timeout)
    # replace the response
    mocker.patch("requests.get", return_value=mock_response)

    assert download_pdf_file.request_html(page_url) == False