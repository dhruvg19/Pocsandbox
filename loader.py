from bs4 import BeautifulSoup
import fitz  # PyMuPDF

def extract_text_from_uploaded_file(fileinfo):
    name = fileinfo['metadata']['name']
    content = fileinfo['content']
    if name.endswith('.pdf'):
        with fitz.open(stream=content, filetype='pdf') as doc:
            return "\n".join(page.get_text() for page in doc)
    elif name.endswith('.html'):
        soup = BeautifulSoup(content.decode('utf-8'), 'html.parser')
        return soup.get_text()
    return ""