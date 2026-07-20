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
                 {/*{recommendation}*/}
                 {
                    " Here are some funny superhero movies that you might enjoy:\n\n---\n## 🎬 The Lego Batman Movie (2017)\n\n**Genres**\n\n- Action\n- Adventure\n- Comedy\n- Animation\n\n**Brief overview** - A fun and hilarious spin on the Dark Knight with a LEGO twist.\n\n**Why it matches 🧐**\n- It features superheroes\n- The movie is known for its humor and comedy elements\n\n---\n## 🎬 Deadpool (2016)\n\n**Genres**\n\n- Action\n- Adventure\n- Comedy\n- Superhero\n\n**Brief overview** - A fourth-wall-breaking antihero with a witty and crude sense of humor.\n\n**Why it matches 🧐**\n- It features superheroes\n- The movie is known for its comedic tone and adult humor\n\n---\n## 🎬 Guardians of the Galaxy (2014)\n\n**Genres**\n\n- Action\n- Adventure\n- Comedy\n- Superhero\n- Sci-fi\n\n**Brief overview** - A group of eccentric and unlikely heroes on a mission to save the galaxy.\n\n**Why it matches 🧐**\n- It features superheroes\n- The movie is known for its humor, wit, and unexpected humor moments\n\n---"
                 }
            </RecommendationPanel>
        </div>
    );
}

export default App;