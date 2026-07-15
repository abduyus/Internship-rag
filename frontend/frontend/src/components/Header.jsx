import styled from "styled-components";

const StyledHeader = styled.header`
    display: flex;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 2.4rem;
    margin-top: 1.6rem;
    font-size: 2.4rem;
    `
const StyledSubheader = styled.span`
    font-size: 1.6rem;
`

function Header() {
    return (
        <StyledHeader>
            <span>Movie Recommendation AI</span>
            <StyledSubheader>Intelligent movie recommendation and booking system using RAG + LangChain</StyledSubheader>

        </StyledHeader>
    );
}

export default Header;