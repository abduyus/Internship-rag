from search import search_movies


def test_search_movies_returns_results():
    results = search_movies('tony stark')
    assert len(results) > 0


def test_search_movies_returns_movie_payload():
    results = search_movies('space exploration')

    movie = results[0]

    assert 'title' in movie.payload
    assert 'overview' in movie.payload


def test_search_movie_finds_iron_man():
    results = search_movies('movie featuring tony stark')

    titles = [movie.payload['title'] for movie in results]

    assert 'Iron Man' in titles
