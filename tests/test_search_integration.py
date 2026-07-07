from search import search_movies

def test_search_movies_returns_results():
    results = search_movies('tony stark')
    assert len(results) > 0