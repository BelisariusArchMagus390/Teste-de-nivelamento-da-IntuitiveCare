from web_scraping_pdf import DownloadPDFFile

page_url = "https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos"
tag = "a"
zip_file_name = "pdf_files.zip"

# creating object
attachment = DownloadPDFFile(page_url)

# make a request 
attachment.request_html()

# search the specified files
attachment_1_link = attachment.search_pdf(tag, "Anexo I.")
attachment_2_link = attachment.search_pdf(tag, "Anexo II.")

# download the files
attachment.download_pdf(attachment_1_link)
attachment.download_pdf(attachment_2_link)

attachment.compact_file(zip_file_name)