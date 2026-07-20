import styled from "styled-components";

const StyledMovieText = styled.h1`
     
       
        text-align: center;
        font-size: 1.8rem;
        grid-row: 1;
    grid-column: span 4;
    
`

function MovieText({children}) {
    return (
        <StyledMovieText>
            {children}
        </StyledMovieText>
    );
}

export default MovieText;