import pytest
from src.backend.models import User, Document

class TestUserModel:
    def test_user_creation(self):
        user = User(username="test", email="test@example.com")
        assert user.username == "test"
        assert user.email == "test@example.com"

    def test_user_password_hashing(self):
        user = User(username="test", email="test@example.com")
        user.set_password("password123")
        assert user.check_password("password123")
        assert not user.check_password("wrong_password")

class TestDocumentModel:
    def test_document_creation(self):
        doc = Document(title="Test Doc", content="Content")
        assert doc.title == "Test Doc"
        assert doc.content == "Content"
