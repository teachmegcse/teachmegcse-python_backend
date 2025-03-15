import os
import shutil

unsorted_dir = r"D:\python_projects\teachmegcse\full_pdfs\9702"
sorted_dir = r"D:\python_projects\teachmegcse\Classified pdfs\9702\long"

files = os.listdir(unsorted_dir)
valid_years = ["19","20","21", "22", "23", "24"]
valid_types = ["qp","ms"]
valid_papers = ["21", "22", "23", "31", "32", "33", "41","42","43", "51", "52", "53", "61", "62", "63"]
for file in files:
    year = file.split("_")[1][1:3]
    type = file.split("_")[2]
    try:
        paper = file.split("_")[3]
        paper = paper.split(".")[0]
    except:
        paper = ""
    if year in valid_years and type in valid_types and paper in valid_papers:
        src = os.path.join(unsorted_dir, file)
        dest = os.path.join(sorted_dir, file)
        shutil.copy(src, dest)
    
