import PyPDF2

def extract_answers_from_pdf(code, pdfName):
    pdfPath = f"D:/python_projects/teachmegcse/full_pdfs/{code}/{code}_{pdfName}.pdf"
    pdf_reader = PyPDF2.PdfReader(open(pdfPath, "rb"))
    text = ""
    for page_num in range(len(pdf_reader.pages)):
        page = pdf_reader.pages[page_num]
        text += page.extract_text()
    lines = text.split('\n')
    answers = []
    for line in lines:
        if line.strip() and line[0].isdigit():
            parts = line.split()
            answer = parts[1] if len(parts) > 1 else ''
            answers.append(answer)
    return answers