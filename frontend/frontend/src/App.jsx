import Header from "./sections/Header.jsx";
import RecommendationPanel from "./sections/RecommendationPanel.jsx";
import {useState} from "react";


const MOCK_RECOMMENDATION =
    {
        "summary": "",
        "movies": [
            {
                "title": "Iron Man",
                "year": 2008,
                "genres": [],
                "overview": "Tony Stark creates an advanced suit of armor and uses it to fight crime.",
                "why_it_matches": [
                    "Starring Tony Stark",
                    "Advanced technology themes"
                ],
                "match_score": 9.573412470645808,
                "rating": 7.9,
                "duration": 126,
                "backdrop_url": "https://image.tmdb.org/t/p/original/cyecB7godJ6kNHGONFjUyVN9OX5.jpg"
            },
            {
                "title": "Iron Man 2",
                "year": 2010,
                "genres": [],
                "overview": "Tony Stark builds an even more advanced suit of armor and faces new threats.",
                "why_it_matches": [
                    "Starring Tony Stark",
                    "Advanced technology themes"
                ],
                "match_score": 9.37846512245098,
                "rating": 7.7,
                "duration": 121,
                "backdrop_url": "https://image.tmdb.org/t/p/original/7lmBufEG7P7Y1HClYK3gCxYrkgS.jpg"
            },
            {
                "title": "Iron Man 3",
                "year": 2013,
                "genres": [],
                "overview": "Tony Stark tries to keep his superhero identity a secret while facing a new enemy.",
                "why_it_matches": [
                    "Starring Tony Stark",
                    "Advanced technology themes"
                ],
                "match_score": 9.165207434798884,
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