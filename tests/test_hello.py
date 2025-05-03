# tests/test_hello.py
from hello import greet  # Assuming hello.py has a function `greet()`

def test_greet():
    assert greet() == "Hello, GitHub Actions!"