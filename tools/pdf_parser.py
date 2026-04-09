import pypdf

def extract_text_from_pdf(file):

    reader = pypdf.PdfReader(file)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text