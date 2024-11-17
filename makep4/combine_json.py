import json
from os.path import exists

subjectcode=9702
subjectname="physics"
jsondirectory=r"D:\python_projects\teachmegcse\python_files\makep4\phy_db_final_p4.json"
MSjsonDirectory=r"D:\python_projects\teachmegcse\python_files\classified\testp4.json"
QuestionJsonDirectory=r"D:\python_projects\teachmegcse\json_files\phy_db_p4.json"

def combineJSON(MSjson,QPjson,jsonDirectory):
    totalData = []
    MSData = json.load(open(MSjson))
    QPData = json.load(open(QPjson))
    if exists(jsonDirectory):
        with open(jsonDirectory, 'r') as f:
            totalData = json.load(f)
    for QPindex in range(len(QPData)):
        MSindex = 0
        while MSindex < len(MSData):
            if MSData[MSindex]["questionNumber"] == QPData[QPindex]["questionNum"] and MSData[MSindex]["paperCode"].replace("ms","qp") == QPData[QPindex]["pdfName"]:
                totalData.append({
                    "questionName": QPData[QPindex]["questionName"],
                    "MSName": MSData[MSindex]["fileName"],
                    "questionNumber": MSData[MSindex]["questionNumber"],
                    "pdfName": QPData[QPindex]["pdfName"]
                })
                break
            MSindex += 1
    with open(jsonDirectory, 'w') as totalJson:
        json.dump(totalData, totalJson, indent=1)

combineJSON(MSjsonDirectory,QuestionJsonDirectory,jsondirectory)