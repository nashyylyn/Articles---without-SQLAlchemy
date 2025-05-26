from lib.models.magazine import Magazine

def test_magazine_articles():
    magazines = Magazine.all()
    tech_weekly = next((m for m in magazines if m.name == "Tech Weekly"), None)
    assert tech_weekly is not None

    articles = tech_weekly.articles()
    assert isinstance(articles, list)
    assert all(hasattr(article, 'title') for article in articles)
