from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

app = FastAPI()

# Pydantic model for the text field
class TextData(BaseModel):
    text: str

# Pydantic model for user data
class UserData(BaseModel):
    name: str
    age: int

# Welcome Note
@app.get("/")
def read_root():
    return {"message": "Welcome to the API! Customized for [Your Name]"}
# FastAPI endpoint to accept POST request with a JSON body containing a single field "text"
# It should return a checksum of the text
@app.post("/generate/")
def generate(data: TextData):
    # Generate a checksum of the text
    checksum = hashlib.md5(data.text.encode()).hexdigest()
    return {"checksum": checksum}

# FastAPI endpoint to accept POST request with a JSON body containing user data
@app.post("/user/")
def create_user(data: UserData):
    return {"name": data.name, "age": data.age}
