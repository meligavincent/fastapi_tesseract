from typing import Annotated

from fastapi import FastAPI, File, UploadFile
import cv2
import pytesseract
import numpy as np

from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import os
import shutil
from model import FileProcessing
from pymongo import MongoClient


app = FastAPI()
app.mount("/files", StaticFiles(directory="files"), name="files")
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



def create_upload_files(files: list[UploadFile]):
   
    for file in files:
        with open(f"files/{file.filename}", "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
    return {"filenames": [file.filename for file in files]}

@app.post("/uploadfiles/")
async def create_upload_file(files: list[UploadFile]) -> list[FileProcessing]:

    file_processing = []
    files = create_upload_files(files=files)["filenames"]

    for file in files:
        if str(file).split(".")[-1] in ["png", "jpg", "PNG", "JPG"]:

            
            img = cv2.imread(f'./files/{file}')
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            threshold_img = cv2.threshold(
                gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
            )[1]
            text = pytesseract.image_to_string(threshold_img)

        else:
            text = None
        
        try :
            os.mkdir('files')
        except OSError:
            print('files folder already created')


        file_processing.append(
            FileProcessing(
                file_path=f"http://localhost:8000/files/{file}",
                file_name=file,
                processed=True,
                extracted_text=text,
            )
        )

        file_data = FileProcessing(
            file_path=f"http://localhost:8000/files/{file}",
            processed=True,
            extracted_text=text,
        ).dict()
        client = MongoClient("mongodb://localhost:27017/")
        db = client["OCR"]
        collection = db["FileProcessing"]
        collection.insert_one(file_data)
    return file_processing


@app.get("/getfiles/")
async def get_files():
    client = MongoClient("mongodb://localhost:27017/")
    db = client["OCR"]
    collection = db["FileProcessing"]
    data = list(
        collection.find(
            {},
            {
                "_id": 0,
                "file_path": 1,
                "file_name": 1,
                "processed": 1,
                "extracted_text": 1,
            },
        )
    )

    return data
