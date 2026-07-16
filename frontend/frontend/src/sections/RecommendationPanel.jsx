import styled from "styled-components";
import ReactMarkdown from "react-markdown";

const StyledRecommendationPanel = styled.div`
    margin: 2.4rem;
    background-color: var(--color-grey-200);
    //background-color: var(--backdrop-color);
    padding: 2rem;
    height: auto;
    border-radius: var(--border-radius-md);
    //box-shadow: var(--shadow-md)
    
    strong {
        font-weight: 800;
        color: var(--color-blue-700);
        margin: 0.8rem;
    }
    
   
    > p:first-of-type {
        margin-bottom: 1rem;
        text-align: center;
        font-size: 2.4rem;
    }
    > p:nth-of-type(2) {
        text-align: center;
        margin-bottom: 2.4rem;
    }
    
`


function RecommendationPanel({children}) {
    console.log(children)
    return (
        <StyledRecommendationPanel>
            <ReactMarkdown>
            {children}
            </ReactMarkdown>
        </StyledRecommendationPanel>
    );
}

export default RecommendationPanel;