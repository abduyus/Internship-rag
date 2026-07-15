from backend.search import deduplicate_results


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


def test_deduplicate_empty_results():
    points = []
    result = deduplicate_results(points)
    assert result == []
