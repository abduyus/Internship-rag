import styled from "styled-components";
import Search from "../components/Search.jsx";

const StyledHeader = styled.header`
    //align-items: center;
    //margin-top: 1.6rem;
    //font-size: 2.4rem;
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    align-items: center;
    height: 7.2rem;
    padding: 0 3.2rem;
    background-color: var(--color-grey-100);
    border-radius: 0.9rem;
    margin: 1.6rem;
    `
// const StyledSubheader = styled.span`
//     font-size: 1.6rem;
// `

function Header() {
    return (
        <StyledHeader>
            <span>Movie Recommendation AI</span>
            <Search/>
            {/*<StyledSubheader>Intelligent movie recommendation and booking system using RAG + LangChain</StyledSubheader>*/}

        </StyledHeader>
    );
}

export default Header;