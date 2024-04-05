
from PIL import Image
import json
from fpdf import FPDF #fpdf2 is required
from PyPDF2 import PdfMerger
subject="physics"
subjectcode="9702"
jsondirectory=f"D:/python_projects/teachmegcse/json_files/physics_db.json"
ChapterNamesJson="D:/python_projects/teachmegcse/json_files/chapters.json"
imagelocation=f"D:/python_projects/teachmegcse/images/unsorted/{subject}/p1/"
outputdirectory=f"D:/python_projects/teachmegcse/python_files/classified/pdfs"
def MakeClassified(jsondirectory, chapterjson, outputdirectory, imagelocation, subject, subjectcode, hasIndex=True, hasAd=True, hasChapterPages=True, hasMS=True):
    listofimages=[""]*10 #temporary image list
    i=0 #total counter
    pagenumber=0
    ChapterPages=[]
    classifiedPDF=FPDF("portrait","pt",[1600,2263])
    tempi=0 #temp counter
    totaly=0 #records y
    yinpage=0
    VerticalLine=Image.open("D:/python_projects/teachmegcse/images/verticalline.png").resize((30,2000)) #importing verticalline, and resizing to fit whole page
    FirstPage=True
    Flag=True #flag that records whether the json file has ended
    chapteri=0 #an index that traverses the chapter json file, to find the specific subject needed
    imgheight=0 #value that records the current questin image height
    QuestionCounter=1 #a value which puts a unique number before each question in the chapter, resets with every new chapter
    NewChapter=False
    Data=json.load(open(jsondirectory,'r'))
    ChapterData=json.load(open(chapterjson,'r'))
    while ChapterData[chapteri]["subject"]!=subject:
        chapteri+=1
    while Flag:
        try: #checks to see that there are still lines in the json file, and breaks the loop, if the json file has been fully searched
            Data[i]["questionName"] 
        except:
            break
        if NewChapter and hasChapterPages:    #checks if flag for new chapter is set and the parameter "hasChapterPages" is True to add a Chapter Page
            classifiedPDF.add_page()
            ChapterPages.append(pagenumber) #stores page number in array to add it to the index later
            classifiedPDF.set_font("Arial", size= 150,style="B")
            classifiedPDF.set_xy(500,800)
            classifiedPDF.cell(w=700,h=500,border=False,txt=f"Chapter {Data[i]['Chapter']}: ", center=True) #puts the chapter number in the middle of the title page
            classifiedPDF.set_xy(800,1200)
            classifiedPDF.set_font("Arial", size=77,style="U")
            classifiedPDF.multi_cell(txt=f"{ChapterData[chapteri]['name'][3:]}", border=False,print_sh=True,w=1000,align="X")
            chapteri+=1
            QuestionCounter=1
            NewChapter=False
            firstQuestioninChapter=True
        elif NewChapter and hasChapterPages==False:
            NewChapter=False
            firstQuestioninChapter=True
        else:
            classifiedPDF.add_page()
            while classifiedPDF.will_page_break(imgheight)==False: #makes sure that the new image doesnt overflow, and all are confined on the page
                if Data[i]["Chapter"]!=Data[i-1]["Chapter"]:
                    if FirstPage and hasAd: #checks if "hasAd" is True and its the first page of document to put ad for teachmeGCSE
                        classifiedPDF.set_xy(700,1131)
                        classifiedPDF.set_font("Arial", size=150)
                        classifiedPDF.cell(txt="teachmegcse.com",center=True)
                        FirstPage=False                        
                    i+=1
                    NewChapter=True
                    break
                else: #loads images into array to prepare it to be copied onto the PDF page
                    if firstQuestioninChapter: #checks if its the first question in the chapter, if it is it decrements i, because it is incrememented during the title page while no image is added
                        firstQuestioninChapter=False
                        i-=1
                    ThisQ=Data[i]["questionName"]
                    Currentimg=Image.open(f"{imagelocation}\{ThisQ}")
                    imgheight=Currentimg.height
                    totaly+=Currentimg.height+200
                    listofimages[tempi]=Currentimg
                    print(i)
                    if totaly>2200: #makes sure that the total y of images of the images is smaller than the page, if it is it breaks, if not it keeps adding new images onto the page
                        break
                    i+=1
                try:
                    Data[i]["questionName"] #checks whether the json file has ended
                except:
                    break
                tempi+=1
            for x in range(tempi): # puts Question Number before image, and loads question images onto the pdf page
                classifiedPDF.set_xy(115,yinpage+230)
                classifiedPDF.set_font("Arial", size=37)
                classifiedPDF.cell(w=3,h=6,border=False,txt=f"{QuestionCounter})")
                QuestionCounter+=1
                classifiedPDF.image(listofimages[x],180,yinpage+200,1420,listofimages[x].height)
                yinpage+=listofimages[x].height+100
            classifiedPDF.set_xy(770,2150)
            classifiedPDF.set_font("Arial", size=55)#puts page number at the bottom of the page
            classifiedPDF.cell(txt=str(pagenumber), center=True)    
        tempi=0
        totaly=0
        yinpage=0
        pagenumber+=1
    if hasIndex:#checks if paramter "hasindex" is set as True by the user
        indexpage=FPDF("portrait","pt",[1600,2263])
        indexpage.add_page()
        indexpage.set_xy(50,100)
        indexpage.set_font("Arial",size=75)
        indexpage.cell(txt="Index", center=True)
        currentx=200
        currenty=300
        secondx=650 #for index only
        for x in range(len(ChapterPages)):
            indexpage.set_xy(currentx, currenty)
            indexpage.set_font("Arial",size=45,style="B") #sets the size and font of the entry in index, and bold as well
            indexpage.cell(txt=f"Chapter {x+1} ")
            indexpage.set_xy(secondx, currenty)
            indexpage.set_font("Arial",size=45,style="")
            indexpage.cell(txt=str(ChapterPages[x]))  #keeps incrementing y value, and copies value of each start of chapter page onto the index
            if currenty>1800: #makes sure index doesnt overflow out of the page
                currentx=secondx+300 #changes x coordinate to second half of the page
                secondx=1450 #position of page number
                currenty=150# resets y to the beggining of the page
                indexpage.image(VerticalLine,x=790,y=500,w=100,h=1122) #loads vertical line which is aesthetically pleasing, after the first row is full
            currenty+=150 #keeps a distance between each index entry
        indexpage.set_xy(currentx,currenty)
        indexpage.set_font("Arial",size=45,style="B") #sets the size of the font
        indexpage.cell(txt="Mark Scheme")
        indexpage.set_font("Arial",size=45,style="")
        indexpage.set_xy(secondx,currenty)
        indexpage.cell(txt=str(pagenumber))  #puts page number at the bottom
    fullPDF=PdfMerger()        
    classifiedPDF.output(f"{outputdirectory}\{subject}_{Data[i-1]['Level']}_p1_classified.pdf")
    if hasIndex:
        indexpage.output(f"{outputdirectory}\{subject}_{Data[i-1]['Level']}_p1_index.pdf")
        fullPDF.append(f"{outputdirectory}\{subject}_{Data[i-1]['Level']}_p1_index.pdf")
        fullPDF.append(f"{outputdirectory}\{subject}_{Data[i-1]['Level']}_p1_classified.pdf")     
        fullPDF.write(f"{outputdirectory}\{subject}_{Data[i-1]['Level']}_p1_classified+index.pdf")  #merges index and classified pdf and outputs it to this folder
        if hasMS:
            MSpath=MakeP1Ms(jsondirectory)
            fullPDF.append(MSpath)
            fullPDF.write(f"{outputdirectory}\{subject}_{Data[i-1]['Level']}_p1_fullclassified.pdf")
    else:
        if hasMS:
            MSpath=MakeP1Ms(jsondirectory)
            fullPDF.append(f"{outputdirectory}\{subject}_{Data[i]['Level']}_p1_classified.pdf")
            fullPDF.append(MSpath)
            fullPDF.write(f"{outputdirectory}\{subject}_{Data[i]['Level']}_p1_classified+ms.pdf")
def MakeP1Ms(jsondirectory):
    i=0
    Flag=True
    FirstQinChapter=False
    FirstQ=True
    yinpage=350
    xinpage=200
    QuestionNumber=1
    QuestionData=json.load(open(jsondirectory,'r'))
    MarkScheme=FPDF(unit="pt",format=[1600,2263])
    while Flag:
        MarkScheme.add_page()
        MarkScheme.set_xy(800,200)
        MarkScheme.set_font('Arial',size=55)
        MarkScheme.cell(txt=f"Chapter: {QuestionData[i]['Chapter']}",center=True)#puts the chapter number at the top of the page
        if FirstQ: #this is donedye to an error which causes the first question to not load
            MarkScheme.set_xy(xinpage,yinpage)
            MarkScheme.set_font("Arial",size=30,style="B") 
            MarkScheme.cell(txt=f"{QuestionNumber})")
            MarkScheme.set_xy(xinpage + 60,yinpage)
            MarkScheme.set_font("Arial",size=30)
            MarkScheme.cell(txt=QuestionData[i]["Answer"])
            QuestionNumber+=1
            print(i)
            i+=1
            FirstQ=False
            yinpage+=40
        while QuestionData[i]['Chapter']==QuestionData[i-1]['Chapter'] or FirstQinChapter: #firstqinchapter is a flag made to avoid the program going into an infinite loop
            MarkScheme.set_xy(xinpage,yinpage)
            MarkScheme.set_font("Arial",size=30,style="B")
            MarkScheme.cell(txt=f"{QuestionNumber})")
            MarkScheme.set_xy(xinpage + 60,yinpage)
            MarkScheme.set_font("Arial",size=30)
            MarkScheme.cell(txt=QuestionData[i]["Answer"]) #imports value of answer from json file
            QuestionNumber+=1
            print(i)
            if QuestionNumber%5==1: #aesthetic feature, does a gap between every 5 questions to make the markscheme more readable
                yinpage+=150
            else:
                yinpage+=40
            if FirstQinChapter:
                FirstQinChapter=False
            try: 
                QuestionData[i+1]["Answer"] #makes sure that the json file hasnt ended, if it has it sets the flaf and breakes the inner loop
            except:
                Flag=False
                break
            i+=1
            if yinpage>2100:
                xinpage+=300
                yinpage=350
            if xinpage>1500: #if the space in the page has ended but there are still more entries
                MarkScheme.add_page() #makes a new page, and initialises x, and y to add more entries to the markscheme
                xinpage=200
                yinpage=350
        FirstQinChapter=True #after loop ends, this means that there are no new entries to the old chapter, and a flag is set for the new chapter, while the y and x values are initialised
        yinpage=350
        xinpage=200
        QuestionNumber=1
    MarkScheme.output(f"{outputdirectory}\{subject}_{QuestionData[0]['Level']}_p{QuestionData[0]['paperNumber']}_ms.pdf")
    return f"{outputdirectory}\{subject}_{QuestionData[0]['Level']}_p{QuestionData[0]['paperNumber']}_ms.pdf" #returns the pdf name so that the parent function can use it to merge both the classified and mark scheme
MakeClassified(jsondirectory, ChapterNamesJson, outputdirectory, imagelocation, subject, subjectcode, False, False, False, True)