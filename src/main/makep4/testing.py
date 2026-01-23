from pdf2image import convert_from_path
import PIL
from PyPDF2 import PdfReader
from tkinter import *
from tkinter import filedialog
import os
import json
import requests
import multiprocessing
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
import re
import cv2
from joblib import load
import shutil
import pdfplumber

BASE_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../..", "src"))
