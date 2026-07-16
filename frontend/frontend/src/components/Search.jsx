import Input from "./Input.jsx";
import styled from "styled-components";
import Button from "./Button.jsx";

const StyledSearch = styled.div`
    width: min(100%, 48rem);
    gap: 1rem;
`

function Search() {
    return (
        <StyledSearch>
            <Input type="text" placeholder={'Ask for movie recommendations ...'} />
            {/*<Button type={'submit'} size={'large'} >*/}
            {/*    Search*/}
            {/*</Button>*/}
        </StyledSearch>
    );
}

export default Search;