from langchain_core.tools import tool

from search import search_movies as search_movies_backend


def movie_booking_tool(movie_title, time):
    return f'Booking Confirmed for {movie_title} at {time}'


def search_movies_tool(query):
    results = search_movies_backend(query)
    return [
        {
            "title": r.payload["title"],
            "overview": r.payload["overview"]
        }
        for r in results[:5]
    ]

@tool
def search_movies(query):
    """Search for movies using semantic search"""
    return search_movies_tool(query)

@tool
def book_movie(movie_title, time):
    """Book a movie viewing at a given time"""
    return movie_booking_tool(movie_title, time)