from lib.models.author import Author

def test_author_can_be_found():
    author = Author.find_by_id(1)
    assert author is not None
    assert author.name == "Jane Doe"  # adjust based on seed data

def test_author_articles():
    author = Author.find_by_id(1)
    articles = author.articles()
    assert isinstance(articles, list)
    assert all(hasattr(article, 'title') for article in articles)

def test_author_magazines():
    author = Author.find_by_id(1)
    magazines = author.magazines()
    assert isinstance(magazines, list)
    assert all(hasattr(mag, 'name') for mag in magazines)
