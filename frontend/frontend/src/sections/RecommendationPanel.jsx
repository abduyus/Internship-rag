import styled from "styled-components";
import ReactMarkdown from "react-markdown";

const StyledRecommendationPanel = styled.div`
    margin: 2.4rem;
    background-color: var(--color-grey-200);
    padding: 2rem;
    height: auto;
    border-radius: var(--border-radius-md);
    //box-shadow: var(--shadow-md)
`


function RecommendationPanel({children}) {
    return (
        <StyledRecommendationPanel>
            <ReactMarkdown>
            {children}
            </ReactMarkdown>
        </StyledRecommendationPanel>
    );
}

export default RecommendationPanel;