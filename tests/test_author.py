import pytest
from lib.models.author import Author

def test_author_can_be_found():
    author = Author.find_by_id(1)
    assert author is not None
    assert author.name == "Jane Doe"

def test_author_articles():
    author = Author.find_by_id(1)
    articles = author.articles()
    assert any(article.title == "AI Advances" for article in articles)

def test_author_magazines():
    author = Author.find_by_id(1)
    magazines = author.magazines()
    assert any(mag.name == "Tech Weekly" for mag in magazines)
