
import React,{ useEffect, useState } from 'react';
import './App.css'
import MovieCard from './MovieCard';
import SearchIcon from './search.svg';




const API_URL = "http://www.omdbapi.com?apikey=b6003d8a";

const App =  () => {
    const [movies,setMovies] = useState([]);
    const [searchTerm,setSearchTerm] = useState("");

    useEffect(() => {
        searchMovies('Batman')
    },[]);

    const searchMovies = async (title) => {
        const response = await fetch(`${API_URL}&s=${title}`);
        const data = await response.json();
        setMovies(data.Search);
    };

    return(
        <div className='app'>
            <h1>Movie Land</h1>
            <div className='search'>
                <input 
                placeholder='Search for movies'
                value={searchTerm}
                onChange={(e) => setSearchTerm(e.target.value)}
                />
                <img 
                src={SearchIcon}
                alt="search"
                onClick={() => {searchMovies(searchTerm)}}
                />
            </div>
            {movies?.length > 0 ? (
                <div className='container'>
                    {movies.map((movie) => (
                        <MovieCard movie={movie} />
                    ))}
                    
                </div>
            ) : (
                <div className='empty'>
                    <h1>No Movies Found</h1>
                </div>
            )}
        </div>
    );
}

export default App;