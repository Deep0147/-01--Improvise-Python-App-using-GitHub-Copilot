"""
API Endpoint Documentation

1. Welcome Note:
   - Method: GET
   - Path: /
   - Response: {"message": "Welcome to the API! Customized for Deep0147"}

2. Generate Checksum:
   - Method: POST
   - Path: /generate/
   - Request Body: {"text": "string"}
   - Response: {"checksum": "string"}
"""

# Pydantic model for the text field
class TextData(BaseModel):
    text: str

# Welcome Note
@app.get("/")
def read_root():
    """Welcome note endpoint returning a customized message."""
    return {"message": "Welcome to the API! Customized for Deep0147"}

# FastAPI endpoint to accept POST request with a JSON body containing a single field "text"
@app.post("/generate/")
def generate(data: TextData):
    """Generate a checksum of the text."""
    checksum = hashlib.md5(data.text.encode()).hexdigest()
    return {"checksum": checksum}
