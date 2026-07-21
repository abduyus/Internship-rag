import Header from "./sections/Header.jsx";
import RecommendationPanel from "./sections/RecommendationPanel.jsx";
import {useState} from "react";


const MOCK_RECOMMENDATION =
    {
        "summary": "Based on your preference for a funny superhero movie, here are some options that might interest you:",
        "movies": [
            {
                "title": "Superhero Movie",
                "year": 2008,
                "genres": [
                    "Action",
                    "Comedy",
                    "Science Fiction"
                ],
                "overview": "The team behind Scary Movie takes on the comic book genre in this tale of Rick Riker, a nerdy teen imbued with superpowers by a radioactive dragonfly.",
                "why_it_matches": [
                    "This movie combines superhero elements with comedy, which should make it both entertaining and funny."
                ],
                "match_score": 0.92
            },
            {
                "title": "Superman",
                "year": 1978,
                "genres": [
                    "Action",
                    "Adventure",
                    "Fantasy",
                    "Science Fiction"
                ],
                "overview": "A mild-mannered reporter named Clark Kent works as a journalist alongside his crush Lois Lane at the Daily Planet. He must summon his superhero alter ego when Lex Luthor threatens to take over the world.",
                "why_it_matches": [
                    "While not primarily a comedy, this classic film has humor and should be enjoyable for fans of both superheroes and comedy."
                ],
                "match_score": 0.78
            },
            {
                "title": "Super",
                "year": 2010,
                "genres": [
                    "Comedy",
                    "Action",
                    "Drama"
                ],
                "overview": "After his wife falls under the influence of a drug dealer, an everyday guy transforms himself into Crimson Bolt, a superhero with the best intentions.",
                "why_it_matches": [
                    "This movie has strong comedy elements and is centered around a hero's journey."
                ],
                "match_score": 0.95
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