from lib.models.article import Article

def test_article_fetch():
    articles = Article.all()
    assert len(articles) > 0
    assert any(article.title == "AI Advances" for article in articles)  # Adjust title per your seed data
