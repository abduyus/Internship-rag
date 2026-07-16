import Header from "./sections/Header.jsx";
import RecommendationPanel from "./sections/RecommendationPanel.jsx";

function App() {
    return (
        <div>
            <Header/>
            <RecommendationPanel>
                {
                     " **Funny Superhero Movies**\n\nHere are some funny superhero films that might tickle your fancy:\n\n1. **Guardians of the Galaxy Vol. 2 (2017)** - The humor in this film comes from the characters' quirky personalities and witty dialogues.\n\n   Reason: This Marvel movie is popular for its comedic elements, set against a backdrop of superhero action.\n\n2. **Deadpool (2016)** - Known for its irreverent humor and fourth-wall breaking, Deadpool offers a unique take on the superhero genre.\n\n   Reason: This R-rated film is praised for its comedic approach to the superhero genre, which distinguishes it from other films in the category.\n\n3. **Thor: Ragnarok (2017)** - The humor in this film stems from its colorful visuals and Chris Hemsworth's lighthearted portrayal of Thor.\n\n   Reason: This Marvel movie stands out for its comedic tone, which adds a fresh twist to the usual superhero action."
                }
            </RecommendationPanel>
        </div>
    );
}

export default App;