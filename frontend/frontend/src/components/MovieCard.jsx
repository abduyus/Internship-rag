import styled from "styled-components";

const StyledMovieCard = styled.div`
    background-color: var(--color-grey-100);
    margin: 1.6rem 0.8rem;
    padding: 1.8rem;
    border-radius: var(--border-radius-lg);
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 1.8rem;
    box-shadow: var(--shadow-md);
    transition: all 0.3s;
    
    

    &:hover {
        box-shadow: var(--shadow-lg);
        
        margin: 2.4rem 0.8rem;
    }
    
    
    > p:nth-of-type(1) {
        grid-column: 1;
    }
    > p:nth-of-type(3) {
        grid-column: 2;
    }

    p:first-of-type + ul{
        display: flex;
        gap: 1.8rem;
        margin-bottom: 1.2rem;
    }
    
    li {
        //background-color: var(--color-grey-600);
    }
    > p:first-of-type + ul li{
         background-color: var(--color-brand-600);
         padding: 0.4rem 1rem;
         border-radius: var(--border-radius-lg);
        font-size: 1.2rem;
        text-transform: uppercase;
     }
    
    ul:last-of-type {
        display: flex;
        flex-direction: column;
        gap: 1.2rem
    }
    
`
function MovieCard({movie}) {
    const {title, genres, overview, why_it_matches, year} = movie;
    console.log(title, genres, overview, why_it_matches, year)

    return (
        <StyledMovieCard>
        </StyledMovieCard>
    );
}

export default MovieCard;