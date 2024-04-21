from pydantic import BaseModel


class FileProcessing(BaseModel):
    file_path: str
    file_name: str | None = None
    processed: bool
    extracted_text: str | None = None
