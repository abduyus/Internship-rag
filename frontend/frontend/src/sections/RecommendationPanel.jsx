import styled from "styled-components";
import ReactMarkdown from "react-markdown";
import MovieText from "../components/MovieText.jsx";
import MovieCard from "../components/MovieCard.jsx";

const StyledRecommendationPanel = styled.div`
    margin: 2.4rem;
    background-color: var(--color-grey-200);
    //background-color: var(--backdrop-color);
    padding: 2rem;
    border-radius: var(--border-radius-md);
    //box-shadow: var(--shadow-md)
    overflow: scroll;
    max-height: 100vh;
    
    strong {
        font-weight: 800;
        color: var(--color-blue-700);
        margin: 0.8rem;
    }
    
`


function RecommendationPanel({children}) {
    const items = children.split("\n---\n")
    console.log(items)
    const heading = items.shift()
    console.log(heading)
    console.log(items)

    return (
        <StyledRecommendationPanel>
            <MovieText>
                {heading}
            </MovieText>
            {items.map(movie => <MovieCard ><ReactMarkdown>{movie}</ReactMarkdown></MovieCard> )}
        </StyledRecommendationPanel>
    );
}

export default RecommendationPanel;