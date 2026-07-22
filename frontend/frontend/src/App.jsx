import Header from "./sections/Header.jsx";
import RecommendationPanel from "./sections/RecommendationPanel.jsx";
import {useState} from "react";


const MOCK_RECOMMENDATION =
    {
        "summary": "",
        "movies": [
            {
                "title": "All Superheroes Must Die",
                "year": 2011,
                "genres": [
                    "Science Fiction",
                    "Thriller"
                ],
                "overview": "While this movie isn't primarily a comedy, it does include elements of humor in the plot.",
                "why_it_matches": [
                    "Includes humor",
                    "Not strictly comedic"
                ],
                "match_score": 0.6234587199951273,
                "rating": 6.1,
                "duration": 98,
                "backdrop_url": "https://image.tmdb.org/t/p/original/vkniCN8rQjpItnP6Pq7K4aAUxok.jpg"
            },
            {
                "title": "Super",
                "year": 2010,
                "genres": [
                    "Comedy",
                    "Action",
                    "Drama"
                ],
                "overview": "This film is known for its humorous approach to superhero narratives and might fit your criteria well.",
                "why_it_matches": [
                    "Humorous superhero narrative",
                    "Comedic tone"
                ],
                "match_score": 0.8567342199951272,
                "rating": 6.9,
                "duration": 101,
                "backdrop_url": "https://image.tmdb.org/t/p/original/5OGrBmi0fWAE6b1R6uv5EnuWOaL.jpg"
            },
            {
                "title": "Iron Man 2",
                "year": 2010,
                "genres": ['Action', 'Comedy', 'Drama'],
                "overview": "Tony Stark builds an even more advanced suit of armor and faces new threats.",
                "why_it_matches": [
                    "Starring Tony Stark",
                    "Advanced technology themes"
                ],
                "match_score": 0.937846512245098,
                "rating": 7.7,
                "duration": 121,
                "backdrop_url": "https://image.tmdb.org/t/p/original/7lmBufEG7P7Y1HClYK3gCxYrkgS.jpg"
            },
            {
                "title": "Iron Man 3",
                "year": 2013,
                "genres": ['Action', 'Comedy'],
                "overview": "Tony Stark tries to keep his superhero identity a secret while facing a new enemy.",
                "why_it_matches": [
                    "Starring Tony Stark",
                    "Advanced technology themes"
                ],
                "match_score": 0.9165207434798884,
                "rating": 7.7,
                "duration": 132,
                "backdrop_url": "https://image.tmdb.org/t/p/original/iVped1djsF0tvGkvnHbzsE3ZPTF.jpg"
            }
        ]
    };



function App() {
    // const [recommendation, setRecommendation] = useState({
    //     summary: "Intelligent movie recommendation and booking system using RAG + LangChain",
    //     movies: [],
    // });
    const [recommendation, setRecommendation] = useState(MOCK_RECOMMENDATION);
    const [isLoading, setIsLoading] = useState(false)


    return (
        <div>
            <Header setRecommendation={setRecommendation} isLoading={isLoading} setIsLoading={setIsLoading}  />
             <RecommendationPanel isLoading={isLoading} recommendation={recommendation}/>


        </div>
    );
}

export default App;