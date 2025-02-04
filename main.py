from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import hashlib

# Initialize the FastAPI application
app = FastAPI()

# Define a Pydantic model for the text field
class TextData(BaseModel):
    text: str

# Define a Pydantic model for user data
class UserData(BaseModel):
    name: str
    age: int

# Define the root endpoint with a welcome message customized for Deepika
@app.get("/")
def read_root():
    """
    Root endpoint that returns a welcome message.

    Returns:
        JSON: A welcome message customized for Deepika.
    """
    return {"message": "Welcome to the API! Customized for Deepika"}

# Define an endpoint to generate a checksum of the provided text
@app.post("/generate/")
def generate(data: TextData):
    """
    Generate an MD5 checksum for the provided text.

    Args:
        data (TextData): A JSON object containing a single field "text".

    Returns:
        JSON: The MD5 checksum of the provided text.
    """
    # Generate a checksum of the text
    checksum = hashlib.md5(data.text.encode()).hexdigest()
    return {"checksum": checksum}

# Define an endpoint to accept user data and return it
@app.post("/user/")
def create_user(data: UserData):
    """
    Accept user data and return it.

    Args:
        data (UserData): A JSON object containing "name" and "age".

    Returns:
        JSON: The provided user data.
    """
    return {"name": data.name, "age": data.age}
