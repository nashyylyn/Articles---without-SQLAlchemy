import pytest
from lib.models.article import Article

def test_article_fetch():
    articles = Article.all()
    assert any(article.title == "AI Advances" for article in articles)
