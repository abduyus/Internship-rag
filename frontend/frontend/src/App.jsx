import Header from "./sections/Header.jsx";
import RecommendationPanel from "./sections/RecommendationPanel.jsx";
import {useState} from "react";


const MOCK_RECOMMENDATION =
{
    "summary": "Let's find a funny superhero movie for you.",
    "movies": [
    {
        "title": "Batman Begins",
        "year": 2005,
        "genres": [
            "Action",
            "Adventure"
        ],
        "overview": "A young Bruce Wayne is driven to become Batman, a symbol of justice in Gotham City, as he seeks revenge against those responsible for his parents' murder.",
        "why_it_matches": [
            "While not strictly comedic, it does include humorous moments and the overall tone of the movie can be quite entertaining."
        ]
    },
    {
        "title": "The Incredibles",
        "year": 2004,
        "genres": [
            "Animation",
            "Action",
            "Comedy"
        ],
        "overview": "When a family's secret abilities are exposed, they go on an adventure to save the world.",
        "why_it_matches": [
            "A true classic of superhero and animated comedy. This movie is filled with humorous situations and witty dialogue."
        ]
    },
    {
        "title": "Superbad",
        "year": 2007,
        "genres": [
            "Comedy",
            "Drama"
        ],
        "overview": "Two high school seniors try to throw the party of a lifetime on their final night before leaving for college.",
        "why_it_matches": [
            "While not a traditional superhero film, it features comedic elements and can be enjoyed by those looking for a fun movie."
        ]
    },
    {
        "title": "Shang-Chi and the Legend of the Ten Rings",
        "year": 2021,
        "genres": [
            "Action",
            "Adventure",
            "Comedy"
        ],
        "overview": "Shang-Chi must confront his past when he is drawn into the mystery of the Ten Rings organization.",
        "why_it_matches": [
            "Although it's an action-packed adventure, there are plenty of humorous moments and clever dialogue."
        ]
    }
]
};



function App() {
    // const [recommendation, setRecommendation] = useState('Intelligent movie recommendation and booking system using RAG + LangChain');
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