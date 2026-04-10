from PyPDF2 import PdfReader

class ReaderAgent:
    def extract(self, file):
        pdf = PdfReader(file)
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""
        return text