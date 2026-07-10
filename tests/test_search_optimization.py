import types

import search


class FakePoint:
    def __init__(self, title, overview):
        self.payload = {"title": title, "overview": overview}


class FakeQueryResult:
    def __init__(self, points):
        self.points = points


class FakeQdrantClient:
    def __init__(self):
        self.calls = []

    def query_points(self, **kwargs):
        self.calls.append(kwargs)
        return FakeQueryResult([
            FakePoint("Iron Man", "A billionaire builds a suit"),
            FakePoint("The Matrix", "A hacker discovers reality"),
        ])


class FakeSentenceTransformer:
    def __init__(self, model_name):
        self.model_name = model_name
        self.calls = []

    def encode(self, text):
        self.calls.append(text)
        return [0.1, 0.2, 0.3]


class FakeCrossEncoder:
    def __init__(self, model_name):
        self.model_name = model_name

    def predict(self, pairs):
        return [0.9 for _ in pairs]


def test_search_movies_reuses_loaded_models(monkeypatch):
    fake_client = FakeQdrantClient()
    monkeypatch.setattr(search, "qdrant_client", fake_client)

    embedding_calls = []
    reranker_calls = []

    def fake_sentence_transformer(model_name):
        embedding_calls.append(model_name)
        return FakeSentenceTransformer(model_name)

    def fake_cross_encoder(model_name):
        reranker_calls.append(model_name)
        return FakeCrossEncoder(model_name)

    monkeypatch.setattr(search, "SentenceTransformer", fake_sentence_transformer)
    monkeypatch.setattr(search, "CrossEncoder", fake_cross_encoder)

    search._embedding_model = None
    search._reranker = None

    search.search_movies("movie about technology")
    search.search_movies("movie about technology")

    assert embedding_calls.count("all-MiniLM-L6-v2") == 1
    assert reranker_calls.count("cross-encoder/ms-marco-MiniLM-L-6-v2") == 1
