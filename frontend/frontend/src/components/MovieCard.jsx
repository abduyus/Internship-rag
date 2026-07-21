import styled from "styled-components";
import Progress from "./Progress.jsx";


const StyledMovieCard = styled.div`
    background-color: var(--color-grey-100);
    //margin: 1.6rem 0.8rem;
    //padding: 1.8rem;
    border-radius: var(--border-radius-lg);
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    //gap: 1.8rem;
    box-shadow: var(--shadow-md);
    transition: all 0.3s;
    grid-row: 2;
    height: 100%;
    padding-bottom: 1.8rem;


    &:hover {
        box-shadow: var(--shadow-lg);


        transform: translateY(-6px);
    }
    
    .top_movie {
        box-shadow: 0 12px 30px rgba(0,0,0,0.65), 0 0 24px rgba(34,197,94,0.48);
    }

    .movie_title {
        //margin-left: 1.8rem;
        margin: 0 1.8rem 1.2rem;
    }

    .overview {
        //margin-left: 1.8rem;
        margin: 0 1.8rem 1.8rem;

        display: -webkit-box;
        -webkit-line-clamp: 4;
        -webkit-box-orient: vertical;
        overflow: hidden;

    }


    .movie_image {
        width: 100%;
        border-top-left-radius: var(--border-radius-lg);
        border-top-right-radius: var(--border-radius-lg);
        transition: transform .3s ease;
    }


    .matches_reason {
        //padding-left: 1.8rem;
        margin: auto 1.8rem 0;
    }

    .card__genres {
        display: flex;
        flex-wrap: wrap;
        gap: 1.2rem;
        font-size: 1.3rem;
        //margin-bottom: 2.4rem;
        //margin-top: 1.2rem;
        //margin-left: 1.8rem;
        margin: 1.8rem;
    }

    .card__genre {
        display: inline-block;
        padding: 0.4rem 0.8rem;
        font-size: 1.2rem;
        text-transform: uppercase;
        color: #333;
        border-radius: 100px;
        font-weight: 600;
    }

    .card__genre.action {
        background-color: #f8d7da;
        color: #721c24;
    }

    .card__genre.science {
        background-color: #d4edda;
        color: #155724;
    }

    .card__genre.fiction {
        background-color: #fff3cd;
        color: #856404;
    }

    .card__genre.adventure {
        background-color: #cce5ff;
        color: #004085;
    }

    .card__genre.comedy {
        background-color: #d1ecf1;
        color: #0c5460;
    }

    .card__genre.animation {
        background-color: #f0abfc;
        color: #701a75;
    }

    .card__genre.crime {
        background-color: #d6d8d9;
        color: #6c757d;
    }

    .card__genre.documentary {
        background-color: #fca5a5;
        color: #7c2d12;
    }

    .card__genre.drama {
        background-color: #d9f99d;
        color: #365314;
    }

    .card__genre.family {
        background-color: #f8d7da;
        color: #721c24;
    }

    .card__genre.fantasy {
        background-color: #d4edda;
        color: #155724;
    }

    .card__genre.fiction {
        background-color: #fff3cd;
        color: #856404;
    }

    .card__genre.foreign {
        background-color: #cce5ff;
        color: #004085;
    }

    .card__genre.history {
        background-color: #d1ecf1;
        color: #0c5460;
    }

    .card__genre.horror {
        background-color: #f0abfc;
        color: #701a75;
    }

    .card__genre.movie {
        background-color: #d6d8d9;
        color: #6c757d;
    }

    .card__genre.music {
        background-color: #fca5a5;
        color: #7c2d12;
    }

    .card__genre.mystery {
        background-color: #d9f99d;
        color: #365314;
    }

    .card__genre.romance {
        background-color: #f8d7da;
        color: #721c24;
    }

    .card__genre.science {
        background-color: #d4edda;
        color: #155724;
    }

    .card__genre.thriller {
        background-color: #fff3cd;
        color: #856404;
    }

    .card__genre.tv {
        background-color: #cce5ff;
        color: #004085;
    }

    .card__genre.war {
        background-color: #d1ecf1;
        color: #0c5460;
    }

    .card__genre.western {
        background-color: #f0abfc;
        color: #701a75;
    }

`
function MovieCard({movie}) {
    const {title, genres, overview, why_it_matches, year, match_score} = movie;
    console.log(title, genres, overview, why_it_matches, year, match_score);

    return (
        <StyledMovieCard>
            <img src={'img_1.png'} alt="Movie Image" className={'movie_image'} />
            <div className="card__genres">
                {genres.map((genre) => {
                    return (
                        <span className={'card__genre ' + genre.toLowerCase()}>{genre}</span>
                    )
                })}
            </div>
            <h1 className={'movie_title'}>{title} ({year})</h1>
            <Progress score={match_score} />
            <p className={'overview'}>{overview}</p>
            <p className={'matches_reason'}>{why_it_matches}</p>




        </StyledMovieCard>
    );
}

export default MovieCard;