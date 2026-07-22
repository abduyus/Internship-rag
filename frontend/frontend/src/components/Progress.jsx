import styled from "styled-components";

const StyledContainer = styled.div`
    display: flex;
    flex-direction: column;
    padding: 0 1.8rem;
    width: 100%;
    margin: 0.8rem 0;
    //align-items: center;
    gap: 1.8rem;
    
`

const StyledProgress = styled.div`
    width: 100%;
    height: 10px;
    background: #374151;
    border-radius: 999px;
    overflow: hidden;
    margin-bottom: 2.4rem;
`;

const Fill = styled.div`
  height: 100%;
  width: ${({ score }) => score * 100}%;
  background: ${({ gradient }) => gradient};
  transition: width 0.4s ease;
`;

const StyledLabel = styled.label`
    //text-align: center;
    font-weight: 600;
    //align-items: center;
    //margin: 0 auto;
`

function Progress({score}) {
    let label;
    let gradient
    if (score >= 0.9) {
        label = "Excellent Match";
        gradient = "linear-gradient(90deg, #10b981, #22c55e)";
    } else if (score >= 0.8) {
        label = "Great Match";
        gradient = "linear-gradient(90deg, #22c55e, #84cc16)";
    } else if (score >= 0.7) {
        label = "Good Match";
        gradient = "linear-gradient(90deg, #84cc16, #bef264)";
    } else if (score >= 0.6) {
        label = "Decent Match";
        gradient = "linear-gradient(90deg, #f59e0b, #fbbf24)";
    } else {
        label = "Possible Match";
        gradient = "linear-gradient(90deg, #ef4444, #f87171)";
    }
    return (
        <StyledContainer>

            <StyledLabel>{Math.round(score * 100)}% • {label}</StyledLabel>
            <StyledProgress>
                <Fill score={score} gradient={gradient} />
            </StyledProgress>
        </StyledContainer>
    );
}

export default Progress;