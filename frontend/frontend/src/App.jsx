import Header from "./sections/Header.jsx";
import RecommendationPanel from "./sections/RecommendationPanel.jsx";
import {useState} from "react";


// const MOCK_RECOMMENDATION =
//     {
//         "summary": "Two superhero movies with comedic elements are suggested: 'Super' (2010) and 'All Superheroes Must Die' (2011). Both have a funny aspect, but 'Super' is more directly focused on humor.",
//         "movies": [
//             {
//                 "title": "Super",
//                 "year": 2010,
//                 "genres": [
//                     "Comedy",
//                     "Action",
//                     "Drama"
//                 ],
//                 "overview": "After his wife falls under the influence of a drug dealer, an everyday guy transforms himself into Crimson Bolt, a superhero with the best intentions, though he lacks for heroic skills.",
//                 "why_it_matches": [
//                     "The movie focuses on humor and features an everyday man turning into a superhero despite lacking heroic abilities."
//                 ],
//                 "match_score": 0.85,
//                 "backdrop_url": "https://image.tmdb.org/t/p/original/5OGrBmi0fWAE6b1R6uv5EnuWOaL.jpg"
//             },
//             {
//                 "title": "All Superheroes Must Die",
//                 "year": 2011,
//                 "genres": [
//                     "Science Fiction",
//                     "Thriller"
//                 ],
//                 "overview": "Masked vigilantes are rendered powerless by their archenemy and are forced to complete deadly tasks in order to save the lives of more than 100 innocent civilians.",
//                 "why_it_matches": [
//                     "This movie includes a comedic element but has a darker, thriller aspect, making it less focused on humor compared to 'Super'."
//                 ],
//                 "match_score": 0.75,
//                 "backdrop_url": "https://image.tmdb.org/t/p/original/vkniCN8rQjpItnP6Pq7K4aAUxok.jpg"
//             }
//         ]
//     };



function App() {
    const [recommendation, setRecommendation] = useState({
        summary: "Intelligent movie recommendation and booking system using RAG + LangChain",
        movies: [],
    });    // const [recommendation, setRecommendation] = useState(MOCK_RECOMMENDATION);
    const [isLoading, setIsLoading] = useState(false)


    return (
        <div>
            <Header setRecommendation={setRecommendation} isLoading={isLoading} setIsLoading={setIsLoading}  />
             <RecommendationPanel isLoading={isLoading} recommendation={recommendation}/>


        </div>
    );
}

export default App;