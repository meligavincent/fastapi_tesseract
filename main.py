from typing import Annotated

from fastapi import FastAPI, File, UploadFile
import cv2 
import pytesseract
import numpy as np
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/files/")
async def create_file(file: Annotated[bytes, File()]):
    return {"file_size": len(file)}


@app.post("/uploadfiles/")
async def create_upload_file(files: list[UploadFile]):

    for file in files :
        print(str(file.filename).split(".")[-1])
        if str(file.filename).split(".")[-1] in  ["png","jpg","PNG","JPG"]:

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

        else : 
            text="pain"
    return {f"{file.filename}": text}