import styled from "styled-components";

const StyledHeader = styled.header`
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 2.4rem;
    margin-top: 1.6rem;
    `


function Header() {
    return (
        <StyledHeader>
            <span>Movie Recommendation AI</span>
            <span>Intelligent movie recommendation and booking system using RAG + LangChain</span>

        </StyledHeader>
    );
}

export default Header;