import ollama

from search import search_movies

question = input('Ask me about movies: ')
results = search_movies(question)
context = ""

# Add movie details to the context for the LLM
for movie in results:
    payload = movie.payload

    context += f"""
    --------------------------------------------
    --------------------------------------------
    Title: {payload['title']}
    Genres: {payload['genres']}
    Director: {payload['director']}
    Overview:
    {payload['overview']} \n
    """

# Build the prompt from the user question and retrieved context
prompt = f"""
You are a movie recommendation assistant.

You MUST follow these rules:
- Only use information from the retrieved movies below.
- Do NOT use external knowledge or prior training.
- Do NOT invent plot details or facts.
- Only describe movies using the provided overviews.
- If information is missing, say "Not available in retrieved data."

Your task:
Recommend movies that match the user's request.

Retrieved Movies:
{context}

User Question:
{question}

Answer in a clear, structured way:
- Recommended movies
- Why they match the request (ONLY using retrieved overviews)
"""

# Send the prompt to the LLM and print the response
response = ollama.chat(
    model="qwen2.5:14b",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

print(response["message"]["content"])
