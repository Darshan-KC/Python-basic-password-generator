import pytest
from main import SimplePassword, IntermediatePassword, StrongPassword

@pytest.fixture
def password_length():
    return 10  # Fixed length for testing

def test_simple_password_length(password_length):
    generator = SimplePassword(password_length)
    password = generator.generate()
    assert len(password) == password_length, "SimplePassword: Incorrect password length"

def test_simple_password_characters(password_length):
    generator = SimplePassword(password_length)
    password = generator.generate()
    assert all('a' <= char <= 'z' for char in password), "SimplePassword: Contains invalid characters"

def test_intermediate_password_length(password_length):
    generator = IntermediatePassword(password_length)
    password = generator.generate()
    assert len(password) == password_length, "IntermediatePassword: Incorrect password length"

def test_intermediate_password_characters(password_length):
    generator = IntermediatePassword(password_length)
    password = generator.generate()
    assert all(('a' <= char <= 'z') or ('A' <= char <= 'Z') for char in password), "IntermediatePassword: Contains invalid characters"

def test_strong_password_length(password_length):
    generator = StrongPassword(password_length)
    password = generator.generate()
    assert len(password) == password_length, "StrongPassword: Incorrect password length"

def test_strong_password_characters(password_length):
    generator = StrongPassword(password_length)
    password = generator.generate()
    valid_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&@")
    assert all(char in valid_chars for char in password), "StrongPassword: Contains invalid characters"
