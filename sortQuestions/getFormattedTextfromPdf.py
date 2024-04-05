import re
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from PyPDF2 import PdfReader

def getPdfText(pdfPath):
    reader = PdfReader(pdfPath)
    numOfPages = len(reader.pages)
    text = ''
    for i in range(numOfPages):
        page = reader.pages[i]
        parts = []
        def visitor_body(text, cm, tm, fontDict, fontSize):
            y = tm[5]
            if y > 40 and y < 720:
                parts.append(text)

        page.extract_text(visitor_text=visitor_body)
        text_body = "".join(parts)
        text += text_body
    return text



def makeText(pdfPath):
        text = getPdfText(pdfPath)
        stop_words = set(stopwords.words('english'))
        stemmer=PorterStemmer()

        # Convert all text to lowercase
        text = text.lower()

        # Remove punctuation, digits, and non-alphabetic characters
        text = re.sub(r'[^\w\s]', '', text)
        text = re.sub(r'\d+', '', text)
        
        # Remove Cambridge command words
        text.replace("analyse",""); text.replace("assess",""); text.replace("calculate","");
        text.replace("comment",""); text.replace("compare",""); text.replace("consider","");
        text.replace("contrast",""); text.replace("define",""); text.replace("describe","");
        text.replace("develop",""); text.replace("discuss",""); text.replace("evaluate","");
        text.replace("explain",""); text.replace("give",""); text.replace("identify","");
        text.replace("justify",""); text.replace("outline",""); text.replace("predict","");
        text.replace("sketch",""); text.replace("state",""); text.replace("suggest","");
        text.replace("summarise",""); text.replace("benefit",""); text.replace("drawback","");
        text.replace("advantage",""); text.replace("disadvantage",""); text.replace("understand","");  text.replace("use",""); 

        # Tokenize text into words
        words = word_tokenize(text)

        # Remove stop words
        words = [w for w in words if w not in stop_words]

        # Stem words
        words = [stemmer.stem(w) for w in words]

        # Join the processed words back into a single string
        return ' '.join(words)


def formatText(text):
    
    stop_words = set(stopwords.words('english'))
    stemmer=PorterStemmer()

    # Convert all text to lowercase
    text = text.lower()

    # Remove punctuation, digits, and non-alphabetic characters
    text = re.sub(r'[^\w\s]', '', text)
    text = re.sub(r'\d+', '', text)
    
    # Remove Cambridge command words
    text = text.replace("analyse",""); text = text.replace("assess",""); text = text.replace("calculate","")
    text = text.replace("comment",""); text = text.replace("compare",""); text = text.replace("consider","")
    text = text.replace("contrast",""); text = text.replace("define",""); text = text.replace("describe","")
    text = text.replace("develop",""); text = text.replace("discuss",""); text = text.replace("evaluate","")
    text = text.replace("explain",""); text = text.replace("give",""); text = text.replace("identify","")
    text = text.replace("justify",""); text = text.replace("outline",""); text = text.replace("predict","")
    text = text.replace("sketch",""); text = text.replace("state",""); text = text.replace("suggest","")
    text = text.replace("summarise",""); text = text.replace("benefit",""); text = text.replace("drawback","")
    text = text.replace("advantage",""); text = text.replace("disadvantage",""); text = text.replace("understand","")
    text = text.replace("use",""); text = text.replace("notes and guidance",""); text = text.replace("candidates should be able to","")
    text = text.replace("show",""); text = text.replace("understanding","")

    # Tokenize text into words
    words = word_tokenize(text)

    # Remove stop words
    words = [w for w in words if w not in stop_words]

    # Stem words
    words = [stemmer.stem(w) for w in words]

    # Join the processed words back into a single string
    return ' '.join(words)
