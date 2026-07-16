import Header from "./sections/Header.jsx";
import RecommendationPanel from "./sections/RecommendationPanel.jsx";

function App() {
    return (
        <div>
            <Header/>
            <RecommendationPanel>
                {
                     " Here are some funny superhero movies that might tickle your fancy:\n\n---\n## Kick-Ass (2010)\n\n**Genres** Action • Comedy\n\n**Why it matches** - Features a regular person becoming a superhero - Has humor and action elements\n\n**Brief overview** Dave Lizewski, an ordinary high school student, decides to become a real-life superhero after getting frustrated by the lack of genuine heroes in his city.\n\n---\n## Deadpool (2016)\n\n**Genres** Action • Comedy\n\n**Why it matches** - Rated R for mature humor and action - Anti-hero with a sarcastic wit\n\n**Brief overview** Wade Wilson, a former special forces operative turned mercenary, is subjected to an experimental treatment that turns him into the unconventional, fourth-wall-breaking superhero known as Deadpool.\n\n---\n## Super (2009)\n\n**Genres** Comedy • Drama • Action\n\n**Why it matches** - An ordinary man becomes a superhero after feeling powerless and ignored - Dark humor throughout the movie\n\n**Brief overview** Frank Darbo, a frustrated middle-aged loser who feels unappreciated by his family and society, dons a homemade superhero suit and fights crime as \"The Crimson Bolt.\"\n\n---\n## Mystery Men (1999)\n\n**Genres** Comedy • Action\n\n**Why it matches** - A group of amateur superheroes band together to save their city - Parodies the superhero genre with humor and wit\n\n**Brief overview** The City of Infinity faces danger from a powerful villain, forcing an unlikely team of inept heroes to rise up and protect their town."
                }
            </RecommendationPanel>
        </div>
    );
}

export default App;