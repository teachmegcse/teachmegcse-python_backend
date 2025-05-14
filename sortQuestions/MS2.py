import PyPDF2
from pathConst import PDF_PATH

def extract_answers_from_pdf(code, pdfName):
    pdfPath = f"{PDF_PATH}/{code}/{pdfName}.pdf"
    pdf_reader = PyPDF2.PdfReader(open(pdfPath, "rb"))
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    
    lines = text.split('\n')
    answers = []
    for line in lines:
        line = line.strip()
        parts = line.split()
        # Check if the line contains a question number followed by an answer
        if len(parts) >= 2 and parts[0].isdigit() and len(parts[1]) == 1 and parts[1].isalpha():
            answer = parts[1]
            answers.append(answer)
    
    return answers