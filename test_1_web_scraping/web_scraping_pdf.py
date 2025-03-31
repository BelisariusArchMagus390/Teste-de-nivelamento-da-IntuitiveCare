import requests
from bs4 import BeautifulSoup
from pathlib import Path
import zipfile

class DownloadPDFFile:
	def __init__(self, page_url):
		self.page_url = page_url
		self.request_response = None
		self.files_directory_path = None

	def request_html(self):
		# request html of the page
		request = requests.get(self.page_url)
		# make verification if was successful the request
		if request.status_code == 200:
			print("Successful request\n")
			self.request_response = request
			return True
		else:
			print("Failed request\n")
			return False

	def search_pdf(self, tag, content_tag):
		# check the request
		if self.request_html():
			html_parsed = BeautifulSoup(self.request_response.text, "html.parser")
			# search the pdf file
			pdf_file = html_parsed.find(tag, string=content_tag)
			# check if exist a link of the pdf
			if pdf_file and "href" in pdf_file.attrs:
				pdf_link = pdf_file["href"]

				print("PDF file found\n")

				return pdf_link
			else:
				print("No PDF file found\n")
		else:
			print("Failed request")

	def download_pdf(self, pdf_link):
		# get the path program.py directory
		actual_directory = Path(__file__).parent
		self.files_directory_path = Path("downloaded_files")
		# create the path of the new directory
		self.files_directory_path = actual_directory.joinpath(actual_directory, self.files_directory_path)

		# check if the directory does not exists and create a new one if doesn't
		if not self.files_directory_path.exists():
			Path(self.files_directory_path).mkdir(exist_ok=True)

		file_name = pdf_link.split("/")[-1]

		file_path = self.files_directory_path.joinpath(self.files_directory_path, file_name)

		response_download_pdf = requests.get(pdf_link)
		if response_download_pdf.status_code == 200:
			# download the pdf
			with open(file_path, "wb") as pdf_file:
				pdf_file.write(response_download_pdf.content)

			print(f"Download Completed of the file {file_name}\n")

			return file_path
		else:
			print("Download failed.\n")
			return None
	
	def compact_file(self, zip_file_name):
		actual_directory = Path(__file__).parent
		# zip file path
		zip_file_name_path = actual_directory.joinpath(actual_directory, zip_file_name)

		# create the zip file
		with zipfile.ZipFile(zip_file_name_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
			# select all the files of the directory "downloaded_files" and write them in the zip file
			for pdf_file in self.files_directory_path.iterdir():
				if pdf_file.is_file():
					zipf.write(pdf_file, pdf_file.name)
		
		print(f"All the files have compacted in the file {zip_file_name}.")