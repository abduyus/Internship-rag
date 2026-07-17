import Input from "./Input.jsx";
import styled from "styled-components";
import {useState} from "react";
import Button from "./Button.jsx";
import {HiArrowCircleUp} from "react-icons/hi";
import SpinnerMini from "./SpinnerMini.jsx";


const StyledSearch = styled.div`
    //width: min(100%, 48rem);
    gap: 1rem;
    display: flex;
`

function Search({ setRecommendation, isLoading, setIsLoading }) {
    const [userRequest, setUserRequest] = useState('')

    const handleSubmit = async function(e) {
        e.preventDefault()
        setUserRequest('')
        setRecommendation('')

            if (!userRequest.trim()) return;
            setIsLoading(true);
            try {
                const res = await fetch("http://localhost:8000/chat", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({
                        message: userRequest,
                    }),
                });

                const data = await res.json();

                setRecommendation(data.response);
                setUserRequest("");
                console.log(data.response);
            } catch (err) {
                console.error(err);
            }
            setIsLoading(false)
        };



    return (
        <StyledSearch>
            <Input type="text" placeholder={'Ask for movie recommendations ...'} value={userRequest}
                   onChange={(e) => setUserRequest(e.target.value)} disabled={isLoading} />
            <Button type="submit" size={'medium'} onClick={handleSubmit} disabled={isLoading}>{isLoading? <SpinnerMini/> : <>Ask <HiArrowCircleUp/></>}</Button>
        </StyledSearch>
    );
}

export default Search;