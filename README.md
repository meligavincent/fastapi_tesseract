# Mees

This is a FastAPI-based service for OCR (Optical Character Recognition). It provides endpoints for uploading image files,, pdf images scanned files  , processing them for text extraction, and retrieving the results. You can also make summarization and translation

## Requirements

- Python 3.7+
- FastAPI
- OpenCV (cv2)
- Pytesseract
- pymongo
- momgodb
- elasticsearch
- RabbitMq



## Installation

Choose one of the following methods to install and run the project:

### Using Virtual Environment (virtualenv)

1. Clone this repository:

   ```bash
   git clone https://github.com/meligavincent/fastapi_tesseract
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi_tesseract
   ```

3. Create a virtual environment:

   ```bash
   virtualenv venv
   ```

4. Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

### Using venv

1. Clone this repository:

   ```bash
   git clone https://github.com/meligavincent/fastapi_tesseract
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi_tesseract
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

6. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

### Using Poetry (Preferred)

1. Clone this repository:

   ```bash
   git clone https://github.com/meligavincent/fastapi_tesseract
   ```

2. Navigate to the project directory:

   ```bash
   cd fastapi_tesseract
   ```

3. Install Poetry (if not already installed):

   ```bash
   curl -sSL https://install.python-poetry.org | python -
   ```

4. Install dependencies and create a virtual environment:

   ```bash
   poetry install
   ```

5. Activate the virtual environment:

   ```bash
   poetry shell
   ```

6. Start the FastAPI server:

   ```bash
   uvicorn main:app --reload
   ```

---

Choose the method that best suits your workflow! Let me know if you need further assistance.
## Usage

### Uploading Files

To upload files, send a POST request to `/uploadfiles/` endpoint with a list of image files. The service supports PNG and JPG formats.

Example using `curl`:

```bash
curl -X 'POST' \
  'http://localhost:8000/uploadfiles/' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@/path/to/your/image1.png' \
  -F 'files=@/path/to/your/image2.jpg'
```

### Retrieving Processed Files

To retrieve processed files, send a GET request to `/getfiles/` endpoint.

Example using `curl`:

```bash
curl -X 'GET' \
  'http://localhost:8000/getfiles/' \
  -H 'accept: application/json'
```

## Configuration

### CORS

By default, the service allows requests from the following origins:

- http://localhost.tiangolo.com
- https://localhost.tiangolo.com
- http://localhost
- http://localhost:8080
- http://localhost:3000

You can modify the CORS settings in the `main.py` file.

### File Storage

Uploaded files are stored in the `files/` directory. You can change the storage directory by modifying the `directory` parameter when mounting the StaticFiles in the `main.py` file.

## Credits

This project was created by MELIGA Vincent Theophane (github : meligavincent).
Linkedin : https://www.linkedin.com/in/vincent-th%C3%A9ophane-meliga-naga-97934b17b/

---

