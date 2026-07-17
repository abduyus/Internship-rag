import Header from "./sections/Header.jsx";
import RecommendationPanel from "./sections/RecommendationPanel.jsx";

function App() {
    return (
        <div>
            <Header/>
            <RecommendationPanel>
                {
                  " Here are some funny superhero movies that were released after 2015:\n\n---\n## Deadpool (2016)\n\n**Genres**\n\n- Action\n- Comedy\n- Superhero\n\n**Brief overview** - A fourth-wall-breaking, R-rated, and over-the-top superhero film that redefined the genre.\n\n**Why it matches**\n- Deadpool is a humorous take on the superhero genre.\n- The film was released in 2016, which satisfies your preference for movies after 2015.\n\n---\n## Guardians of the Galaxy Vol. 2 (2017)\n\n**Genres**\n\n- Action\n- Comedy\n- Superhero\n- Sci-fi\n\n**Brief overview** - A sequel to the hit movie Guardians of the Galaxy, following the ragtag team of superheroes on another cosmic adventure.\n\n**Why it matches**\n- Guardians of the Galaxy Vol. 2 is a humorous superhero film with lots of comedy and action scenes.\n- The film was released in 2017, which satisfies your preference for movies after 2015.\n\n---\n## Spider-Man: Homecoming (2017)\n\n**Genres**\n\n- Action\n- Comedy\n- Superhero\n\n**Brief overview** - A high school-focused reboot of the popular Spider-Man series, following Peter Parker as he juggles his ordinary life and superhero duties.\n\n**Why it matches**\n- Spider-Man: Homecoming is a humorous take on the superhero genre with comedic elements.\n- The film was released in 2017, which satisfies your preference for movies after 2015.\n\n---\n\nI found three funny superhero movies that fit your criteria. Enjoy! If you want to book tickets, please let me know the movie and preferred time."
                }
            </RecommendationPanel>
        </div>
    );
}

export default App;