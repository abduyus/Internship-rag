import Header from "./sections/Header.jsx";
import RecommendationPanel from "./sections/RecommendationPanel.jsx";

function App() {
    return (
        <div>
            <Header/>
            <RecommendationPanel>
                Here are some funny superhero movies that you might enjoy:

                1. Megamind (2010) - Directed by Tom McGrath, this animated film stars Will Ferrell as the title character, a supervillain who decides he wants to become a hero instead. The movie is full of humor and action.

                2. Superhero Movie (2008) - Directed by Craig Mazin, this comedy follows the story of Rick Riker, a high school student who is chosen to save the world from evil as the superhero "The Protoman." The film is filled with parodies of various superhero movies.

                3. All Superheroes Must Die (2011) - Directed by Jason Trost, this thriller follows a group of vigilantes who team up to take down a mysterious serial killer known as "The Prowler." The film combines elements of comedy and action.

                4. Batman v Superman: Dawn of Justice (2016) - Directed by Zack Snyder, while not primarily a comedy, this film does have some humorous moments between Batman (Ben Affleck) and Superman (Henry Cavill). The film is packed with action and an epic battle between the two titular characters.
            </RecommendationPanel>
        </div>
    );
}

export default App;