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
    text.replace("analyse",""); text.replace("assess",""); text.replace("calculate","")
    text.replace("comment",""); text.replace("compare",""); text.replace("consider","")
    text.replace("contrast",""); text.replace("define",""); text.replace("describe","")
    text.replace("develop",""); text.replace("discuss",""); text.replace("evaluate","")
    text.replace("explain",""); text.replace("give",""); text.replace("identify","")
    text.replace("justify",""); text.replace("outline",""); text.replace("predict","")
    text.replace("sketch",""); text.replace("state",""); text.replace("suggest","")
    text.replace("summarise",""); text.replace("benefit",""); text.replace("drawback","")
    text.replace("advantage",""); text.replace("disadvantage",""); text.replace("understand","")
    text.replace("use",""); text.replace("notes and guidance",""); text.replace("candidates should be able to","")
    text.replace("show",""); text.replace("understanding","")

    # Tokenize text into words
    words = word_tokenize(text)

    # Remove stop words
    words = [w for w in words if w not in stop_words]

    # Stem words
    words = [stemmer.stem(w) for w in words]

    # Join the processed words back into a single string
    return ' '.join(words)
