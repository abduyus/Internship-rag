import os

import requests

TMDB_TOKEN = os.getenv("TMDB_API_TOKEN")

HEADERS = {
    "Authorization": f"Bearer {TMDB_TOKEN}"
}


def get_backdrop(title, year):
    print(title)
    print(year)
    response = requests.get(
        "https://api.themoviedb.org/3/search/movie",
        headers=HEADERS,
        params={
            "query": title,
            "year": year,
        },
    )

    data = response.json()

    if not data["results"]:
        return None

    backdrop = data["results"][0].get("backdrop_path")

    if backdrop is None:
        return None

    return f"https://image.tmdb.org/t/p/original{backdrop}"
