
import numpy as np
import pytesseract
import pandas as pd
from PIL import Image
import cv2
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt



# Load the low resolution image
image = cv2.imread('ea.jpg',0)




pytesseract.pytesseract.tesseract_cmd = 'C:/Users/meren/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
custom_oem_psm_config = r'--oem 3 --psm 4'


# Open the image and perform OCR on it
text = pytesseract.image_to_string(image,config=custom_oem_psm_config, lang='tur')

# Split the text into lines and find the lines that contain the table data
lines = text.split('\n')
table_lines = [line for line in lines if line.strip() != '']

# Create a Pandas dataframe from the table data
df = pd.DataFrame([line.split('\t') for line in table_lines])

# Print the dataframe
print(df)



