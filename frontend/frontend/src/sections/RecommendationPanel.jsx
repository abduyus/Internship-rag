import styled from "styled-components";
import ReactMarkdown from "react-markdown";

const StyledRecommendationPanel = styled.div`
    margin: 2.4rem auto;
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