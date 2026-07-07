from search import deduplicate_results, rerank_results


class MockPoint:
    def __init__(self, title):
        self.payload = {
            "title": title
        }


def test_deduplicate_results():
    points = [
        MockPoint('Iron Man'),
        MockPoint('Iron Man'),
        MockPoint('Spiderman'),
    ]

    result = deduplicate_results(points)

    assert len(result) == 2


def test_deduplicate_removes_duplicate_title():
    points = [
        MockPoint('Iron Man'),
        MockPoint('Iron Man'),
        MockPoint('Spiderman'),
    ]

    result = deduplicate_results(points)

    titles = [
        movie.payload['title']
        for movie in result
    ]

    assert titles == ['Iron Man', 'Spiderman']


class RerankMockPoint:
    def __init__(self, title, overview):
        self.payload = {
            "title": title,
            "overview": overview
        }


def test_rerank_results(monkeypatch):
    points = [
        RerankMockPoint('Iron Man', 'overview A'),
        RerankMockPoint('Spiderman', 'overview B'),
        RerankMockPoint('Jamal Khan', 'overview C'),
    ]

    class FakeReranker:
        def predict(self, _):
            return [0.1, 0.9, 0.5]

    monkeypatch.setattr('search.CrossEncoder', lambda *args, **kwargs: FakeReranker())
    result = rerank_results('funny superhero movie', points)

    titles = [
        movie.payload['title']
        for movie in result
    ]

    assert titles == ['Spiderman', 'Jamal Khan', 'Iron Man']
