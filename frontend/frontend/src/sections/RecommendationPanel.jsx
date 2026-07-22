import styled from "styled-components";
import MovieText from "../components/MovieText.jsx";
import MovieCard from "../components/MovieCard.jsx";
import Spinner from "../components/Spinner.jsx";

const StyledRecommendationPanel = styled.div`
    margin: 2.4rem;
    padding: 2rem;

    background-color: var(--color-grey-200);
    border-radius: var(--border-radius-md);

    display: grid;
    grid-template-columns: repeat(${props => props.columns}, 1fr);
    gap: 2.4rem;
    align-items: stretch;
    justify-content: center;

    transition: all 0.3s;

    strong {
        font-weight: 800;
        color: var(--color-blue-700);
    }
`;

const StyledHeading = styled.div`
    grid-column: 1 / -1;
    justify-self: center;
`;

function RecommendationPanel({ recommendation, isLoading }) {
    const heading = recommendation.summary;
    const items = recommendation.movies;
    console.log(items);
    const sorted = [...items].sort((a, b) => b.match_score - a.match_score);
    return (
        <StyledRecommendationPanel
            columns={Math.max(1, Math.min(sorted?.length, 4))}
        >
            {isLoading && <Spinner />}

            <StyledHeading>
                <MovieText>{heading}</MovieText>
            </StyledHeading>

            {sorted?.map((movie, index) => (
                <MovieCard
                    key={movie.title}
                    movie={movie}
                    index={index}
                />
            ))}
        </StyledRecommendationPanel>
    );
}

export default RecommendationPanel;