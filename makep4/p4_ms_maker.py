
from PIL import Image
from pdf2image import convert_from_path
import pytesseract
from os.path import exists
import json

def searchinx(img,searchcolour,constanty:int, startofimg=True ,doublecheck=False):
    currentpixel=img.load()
    if startofimg:
        start=0
        end=img.width-1
        step=1
    else:
        start=img.width-1
        end=0
        step=-1
    for i in range(start,end,step):
        if currentpixel[i,constanty]==searchcolour:
            if doublecheck:
                if currentpixel[i+1,constanty]==searchcolour:
                    return i
            else:
                return i
    return -1
def searchiny(img,searchcolour,constantx:int,startofimg=True,doublecheck=False,notColour=False):
    currentpixel=img.load()    
    if startofimg:
        start=0
        end=img.height-1
        step=1
    else:
        start=img.height-1
        end=0
        step=-1
    if notColour:
        for i in range(start,end,step):
            if currentpixel[constantx,i]!=searchcolour:
                if doublecheck:
                    if currentpixel[constantx,i+1]!=searchcolour:
                        return i
                else:
                    return i
    else:
        for i in range(start,end,step):
            if currentpixel[constantx,i]==searchcolour:
                if doublecheck:
                    if currentpixel[constantx,i+1]==searchcolour:
                        return i
                else:
                    return i
    return -1

def combinearrayImages(imageArray:list,savepath):
    x=imageArray[0].width
    y=0
    for image in imageArray:
        y+=image.height
    if len(imageArray)==1:
        imageArray[0].save(savepath)
    else: #merges all the images in the array if theres more than one image
        currenty=0
        newimage=Image.new('RGB',[x,y], (255,255,255))
        for image in imageArray:
            newimage.paste(image,(0,currenty))
            currenty+=image.height
        newimage.save(savepath)


myoutputdirectory=r"D:\python_projects\teachmegcse\images\ms"
myjsonfilelocation=r"D:\python_projects\teachmegcse\python_files\classified\testp4.json"
pytesseract.pytesseract.tesseract_cmd = r"D:\python_projects\Tesseract-OCR\tesseract.exe"
firstimg=False
skippages=7
def makeQuestionMs(MSpdf,subjectName, subjectcode):
    mypdfDirectory=f"D:/python_projects/teachmegcse/full_pdfs/{subjectcode}" 
    questionNumber=1 #a value that is compared to the text in the start of the iamges to find out whether a new question has started
    endofQ=False #flag used to differentiate between page end and question end since different actions are taken for both
    totalPages=convert_from_path(f"{mypdfDirectory}/{MSpdf}", poppler_path=r"D:\python_projects\poppler-23.05.0\Library\bin") #converts the pdf to a series of images
    currentQuestion=[] #stores images that are within the same question
    MSpages=[] #records only the relevant pages in totalPages array, removes all of the examiner notices
    firstPage=False
    firstJson=True
    MSData=[]
    currentfilenumber=1
    if exists(myjsonfilelocation):
        with open(myjsonfilelocation,'r') as jsonfile:
            MSData=json.load(jsonfile)
            firstJson=False
    while exists(f"{myoutputdirectory}\{subjectName}_ms_{currentfilenumber}.jpg"):
        print(currentfilenumber)
        currentfilenumber+=1
    for i in range(3,len(totalPages)):
        thisPage=totalPages[i].crop(( searchinx(totalPages[i],(0,0,0),210),searchiny(totalPages[i],(0,0,0),500)+68,searchinx(totalPages[i],(0,0,0),210,startofimg=False), searchiny(totalPages[i],(0,0,0),500,False)))
        if firstPage:
            MSpages.append(thisPage)
            thisPage.save(f"{myoutputdirectory}\{subjectName}_page_{i}.jpg")
        print(pytesseract.image_to_string(thisPage)[0])
        if pytesseract.image_to_string(thisPage)[0]=="1" and firstPage==False:
            firstPage=True
            MSpages.append(thisPage)
            thisPage.save(f"{myoutputdirectory}\{subjectName}_page_{i}.jpg")
    for page in MSpages:
        firstNum=pytesseract.image_to_string(page)[0]
        if int(firstNum)==1 and questionNumber>7:
            firstNum=pytesseract.image_to_string(page)[:2]
        print(f"{firstNum}: tesseract") #reads the first text in ocr image
        if firstNum=="A": 
            firstNum=4
        if firstNum=="B": 
            firstNum=6
        if questionNumber!=int(firstNum): #compares the first number in page to the question number to check if a new question has started
            combinearrayImages(currentQuestion,f"{myoutputdirectory}\{subjectName}_ms_{currentfilenumber}.jpg")
            if firstJson: 
                MSData=[{"fileName": f"{subjectName}_ms_{currentfilenumber}", "questionNumber":questionNumber, "paperCode":MSpdf}]
                firstJson=False
            else: 
                MSData.append({"fileName": f"{subjectName}_ms_{currentfilenumber}", "questionNumber":questionNumber, "paperCode":MSpdf})
            currentfilenumber+=1
            questionNumber+=1
            endofQ=False
            currentQuestion=[] #initialises the array so a new question can be added into the array
        pixel=page.load() 
        y=0
        pixelcolour=pixel[0,y]
        while pixelcolour !=(255,255,255)  and y<page.height: #makes sure that the line of reference isnt over
            pixelcolour=pixel[0,y]
            if pixelcolour==(255,255,255):
                    pixelcolour=pixel[0,y+1]
                    if pixelcolour==(255,255,255): #the comparison is done twice due to some error pixels in the pdf in the middle of the line
                        endofQ=True
                        print(1)
                        break #if the line has ended it means that the question has ended or its the end of the page
            y+=1
        if endofQ:
            currentQuestion.append(page.crop((0,0,page.width,y))) #crops the image to the point where the question ended and puts it into the currentquestion array
            print(len(currentQuestion), "len")
            combinearrayImages(currentQuestion,f"{myoutputdirectory}\{subjectName}_ms_{currentfilenumber}.jpg")
            if firstJson:
                MSData=[{"fileName": f"{subjectName}_ms_{currentfilenumber}", "questionNumber":questionNumber, "paperCode":MSpdf}]
                firstJson=False
            else:
                MSData.append({"fileName": f"{subjectName}_ms_{currentfilenumber}", "questionNumber":questionNumber, "paperCode":MSpdf})
            questionNumber+=1
            currentfilenumber+=1
            if y<page.height:  #checks if its the end of the page, if not, the rest is put into an array and stored as the new image
                currentQuestion=[page.crop((0,y+114,page.width,page.height))] #crops from where the first question stopped to the end of the page
                endofQ=False
        else: 
            currentQuestion.append(page)
    if len(currentQuestion)!=0: #checks if there are any items remaining in currentquestion array, and saves all of the data in it into a new iamge
        combinearrayImages(currentQuestion,f"{myoutputdirectory}\{subjectName}_ms_{currentfilenumber}.jpg")
        MSData.append({"fileName": f"{subjectName}_ms_{currentfilenumber}", "questionNumber":questionNumber, "paperCode":MSpdf})
    with open(myjsonfilelocation,'w') as jsonfile: 
        json.dump(MSData,jsonfile,indent=1) #saves the data to the json file

makeQuestionMs("9702_w19_ms_41.pdf", 'physics', 9702) 