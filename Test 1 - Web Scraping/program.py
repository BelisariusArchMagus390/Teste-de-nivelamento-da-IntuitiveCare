from web_scraping_pdf import DownloadPDFFile

page_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
tag = "a"
zip_file_name = "pdf_files.zip"

# creating object
annex = DownloadPDFFile(page_url)

# make a request 
annex.request_html()

# search the specified files
annex_1_link = annex.search_pdf(tag, "Anexo I.")
annex_2_link = annex.search_pdf(tag, "Anexo II.")

# download the files
annex.download_pdf(annex_1_link)
annex.download_pdf(annex_2_link)

annex.compact_file(zip_file_name)