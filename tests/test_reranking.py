from search import rerank_results


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


def test_rerank_empty_results(monkeypatch):
    result = rerank_results('funny superhero movie', [])

    assert result == []
