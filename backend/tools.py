from langchain_core.tools import tool

from backend.search import search_movies as search_movies_backend


def movie_booking_tool(movie_title, time):
    return f'Booking Confirmed for {movie_title} at {time}'


def search_movies_tool(query, min_year=None, max_year=None):
    results = search_movies_backend(query)
    filtered = [
        {
            "title": r.payload["title"],
            "genres": r.payload["genres"],
            "release_date": r.payload["release_date"],
            "director": r.payload["director"],
            "cast": r.payload["cast"],
        }
        for r in results[:5]
        if (min_year is None or int(r.payload["release_date"][:4]) >= min_year) and
           (max_year is None or int(r.payload["release_date"][:4]) <= max_year)
    ]
    return filtered


@tool
def search_movies(query, min_year: int = None, max_year: int = None):
    """ Search the movie database for information about movies.

    Use this tool whenever the user asks about:
    - movie recommendations
    - similar movies
    - genres
    - release dates
    - movie details

    Input:
        query (str): The user's movie-related query.

    Returns:
        A list of matching movies with title, genres and release date.

    Use min_year/max_year to filter by release date.
    Example: search for movies about action released after 2015: search_movies("action", min_year=2015)    
    """
    return search_movies_tool(query, min_year, max_year)


@tool
def book_movie(movie_title, time):
    """ Book a cinema ticket.

    Use this tool only when the user explicitly asks to book or reserve a movie.

    Inputs:
        movie_title (str)
        time (str)

    Returns:
        A booking confirmation."""
    return movie_booking_tool(movie_title, time)
