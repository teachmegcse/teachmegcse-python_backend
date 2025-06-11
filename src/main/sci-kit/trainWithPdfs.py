import getFormattedTextfromPdf
import trainModels
import os

text = ['' for k in range(1,12)]
labels = ['User-Defined-Data-types', 'File-Organisation', 
             'Floating-Point', 'Protocols', 'Circuits-Packets', 
             'Risc-Cisc', 'Boolean-Algebra', 'OS', 'Translation', 
             'Security', 'AI']

# Get a list of all the files in the directory

# Print the list of files
for j in range(1,11):
    path = f"C:/Users/donat/Documents/python_projects/js_test/Classified/sorted/9618/p3/{j}"
    files = os.listdir(path)
    print(files)
    for file in files:
        pdfText = getFormattedTextfromPdf.makeText(f"{path}/{file}")
        print(f"{file} : Done : {labels[j]}")
        text[j-1] += pdfText
trainModels.train(text, labels)
print(text)
print(labels)
