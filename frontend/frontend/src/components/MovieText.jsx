import styled from "styled-components";

const StyledMovieText = styled.h1`
     
        margin-bottom: 1rem;
        text-align: center;
        font-size: 1.8rem;
    
`

function MovieText({children}) {
    return (
        <StyledMovieText>
            {children}
        </StyledMovieText>
    );
}

export default MovieText;