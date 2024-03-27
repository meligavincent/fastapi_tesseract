from typing import Annotated

from fastapi import FastAPI, File, UploadFile
import cv2
import pytesseract
import numpy as np


app = FastAPI()


@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    img = await file.read()
    nparr = np.fromstring(img, np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Apply threshold to convert to binary image
    threshold_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    # Pass the image through pytesseract
    text = pytesseract.image_to_string(threshold_img)
    # Print the extracted text
    print(text)
    return {f"{file.filename}": text}