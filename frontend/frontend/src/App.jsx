import Header from "./sections/Header.jsx";
import RecommendationPanel from "./sections/RecommendationPanel.jsx";
import {useState} from "react";


function App() {
    const [recommendation, setRecommendation] = useState('Intelligent movie recommendation and booking system using RAG + LangChain');
    const [isLoading, setIsLoading] = useState(false)
    return (
        <div>
            <Header setRecommendation={setRecommendation} isLoading={isLoading} setIsLoading={setIsLoading} />
             <RecommendationPanel isLoading={isLoading}>
                 {recommendation}
            </RecommendationPanel>
        </div>
    );
}

export default App;