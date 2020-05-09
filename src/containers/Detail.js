import React from 'react';
import {Container} from "semantic-ui-react";
import axios from 'axios';
import {API_URL} from "../constants";

class Detail extends React.Component {
    state = {
        movie: {}
    };

    componentDidMount() {
        this.fetchMovieDetail()
    }

    fetchMovieDetail = () => {
        const id = this.props.match.params.id;
        axios.get(`${API_URL}/api/movie/${id}`)
            .then(res => {
                console.log(res.data)
                this.setState({movie: res.data})
            })
    };

    render() {
        const {movie} = this.state;
        return (
            <Container style={{marginBottom: '600px'}}>
                <h1>{movie.title}</h1>
                <iframe width="100%" height="500" src={movie.trailer} frameBorder="0"
                        allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                        allowFullScreen></iframe>
                <h1>Story line</h1>
                <p>{movie.story}</p>

                <h2>Download link</h2>
                <p>Size: {movie.download_size}</p>
                <a href={movie.download} download>Torrent download</a>
            </Container>

        )
    }
}

export default Detail;