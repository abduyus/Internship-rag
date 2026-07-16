import styled from "styled-components";

const StyledMovieCard = styled.div`
    background-color: var(--color-grey-100);
    margin: 1.6rem 0.8rem;
    padding: 1.8rem;
    border-radius: var(--border-radius-lg);
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1rem;
    
    
    > p:nth-of-type(1) {
        grid-column: 1;
    }
    > p:nth-of-type(3) {
        grid-column: 2;
    }
`
function MovieCard({children}) {
    console.log(children)
    return (
        <StyledMovieCard>
            {children}
        </StyledMovieCard>
    );
}

export default MovieCard;