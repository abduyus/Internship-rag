import styled from "styled-components";
import MovieText from "../components/MovieText.jsx";
import MovieCard from "../components/MovieCard.jsx";
import Spinner from "../components/Spinner.jsx";

const StyledRecommendationPanel = styled.div`
    margin: 2.4rem;
    background-color: var(--color-grey-200);
    //background-color: var(--backdrop-color);
    padding: 2rem;
    border-radius: var(--border-radius-md);
    //box-shadow: var(--shadow-md)
    overflow: scroll;
    
    transition: all 1s;
    
    strong {
        font-weight: 800;
        color: var(--color-blue-700);
        //margin: 0.8rem;
    }

    
    
`


function RecommendationPanel({recommendation, isLoading}) {
    const heading = recommendation.summary
    const items = recommendation.movies
    console.log(heading, items)

    return (
        <StyledRecommendationPanel>
            {isLoading && <Spinner/>}
            <MovieText>
                {heading}
            </MovieText>
            {items.map(movie => <MovieCard movie={movie} />)}
        </StyledRecommendationPanel>)
}

export default RecommendationPanel;