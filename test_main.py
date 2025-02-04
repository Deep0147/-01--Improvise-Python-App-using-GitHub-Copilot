from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_generate_valid_text():
    """
    Test case for valid text input.
    """
    response = client.post("/generate/", json={"text": "hello"})
    assert response.status_code == 200
    assert response.json() == {"checksum": "5d41402abc4b2a76b9719d911017c592"}

def test_generate_empty_text():
    """
    Test case for empty text input.
    """
    response = client.post("/generate/", json={"text": ""})
    assert response.status_code == 200
    assert response.json() == {"checksum": "d41d8cd98f00b204e9800998ecf8427e"}

def test_generate_special_characters():
    """
    Test case for text input with special characters.
    """
    response = client.post("/generate/", json={"text": "!@#$%^&*()"})
    assert response.status_code == 200
    assert response.json() == {"checksum": "14c4b06b824ec593239362517f538b29"}

def test_generate_long_text():
    """
    Test case for long text input.
    """
    long_text = "a" * 1000
    response = client.post("/generate/", json={"text": long_text})
    assert response.status_code == 200
    # Expected checksum for 1000 'a' characters
    assert response.json() == {"checksum": "cabe45dcc9ae5b66ba86600cca6b8ba8"}
