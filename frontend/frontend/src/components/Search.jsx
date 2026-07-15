import Input from "./Input.jsx";
import styled from "styled-components";
import Button from "./Button.jsx";

const StyledSearch = styled.div`
    margin: 2.4rem auto 0;
    width: 75%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 1rem;
`

function Search() {
    return (
        <StyledSearch>
            <Input type="text" placeholder={'Recommend me a movie ...'}/>
            <Button type={'submit'} size={'large'}>
                Search
            </Button>
        </StyledSearch>
    );
}

export default Search;