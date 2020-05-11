import React from 'react';
import axios from 'axios';
import {API_URL} from "../constants";
import {Link} from "react-router-dom";

class HomepageLayout extends React.Component {
    state = {
        movieList: [],
        searchValue: ''
    };

    componentDidMount() {
        this.movieListRender()
    }

    movieListRender() {
        axios.get(`${API_URL}/api/movie`)
            .then(res => {
                console.log(res.data)
                this.setState({movieList: res.data})
            })
    }

    searchFetch = (e) => {
        e.preventDefault()
        const {searchValue} = this.state;
        axios.get(`${API_URL}/api/search?q=${searchValue}`)
            .then(res => {
                console.log(res.data)
                this.setState({movieList: res.data})

            })
    };

    searchInput = (e) => {
        this.setState({searchValue: e.target.value})
    };

    render() {
        const {movieList} = this.state;
        return (
            <div className="w3_content_agilleinfo_inner">
                <div className="agile_featured_movies">
                    <div className="side-bar-form col-md-12">
                        <form>
                            <input type="search" name="movie" placeholder="Search here...."
                                   required="required" onChange={this.searchInput}/>
                            <input type="submit" onClick={this.searchFetch} value=" "/>
                        </form>
                    </div>
                    <div className="agileinfo_tabs">
                        <div id="horizontalTab">
                            <ul className="resp-tabs-list">
                                <li>Recent</li>
                                <li>Popularity</li>
                                <li>Top Rating</li>

                            </ul>
                            <div className="resp-tabs-container">
                                <div className="tab1">
                                    <div className="tab_movies_agileinfo">
                                        <div className="w3_agile_featured_movies">
                                            <div className="col-md-12 wthree_agile-movies_list">
                                                {movieList.map(movie => {
                                                    return (
                                                        <div className="w3l-movie-gride-agile">
                                                            <Link to={`/movie/${movie.id}`}
                                                                  className="hvr-sweep-to-bottom"><img
                                                                src={movie.image}
                                                                title="Movies Pro"
                                                                className="img-responsive"
                                                                alt=" "/>
                                                                <div className="w3l-action-icon"><i
                                                                    className="fa fa-play-circle-o"
                                                                    aria-hidden="true"></i></div>
                                                            </Link>
                                                            <div className="mid-1 agileits_w3layouts_mid_1_home">
                                                                <div className="w3l-movie-text">
                                                                    <h6><a href="single.html">{movie.title}</a></h6>
                                                                </div>
                                                                <div className="mid-2 agile_mid_2_home">
                                                                    <p>{movie.release_date}</p>

                                                                    <div className="block-stars">
                                                                        <ul className="w3l-ratings">
                                                                            <li><i className="fa fa-star"
                                                                                   aria-hidden="true"></i>{movie.rating}
                                                                            </li>
                                                                        </ul>
                                                                        {/*<p>*/}
                                                                        {/*    <a href={movie.download}*/}
                                                                        {/*       download={movie.download}>*/}
                                                                        {/*        Torrent Download*/}
                                                                        {/*    </a>*/}

                                                                        {/*</p>*/}
                                                                    </div>
                                                                    <div className="clearfix"></div>

                                                                </div>
                                                            </div>
                                                            <div className="ribben">
                                                                <p>NEW</p>
                                                            </div>
                                                        </div>
                                                    )
                                                })}


                                            </div>
                                            <div className="clearfix"></div>
                                        </div>
                                        <div className="cleafix"></div>
                                    </div>
                                </div>
                            </div>
                        </div>

                    </div>



                </div>
            </div>


        )
    }
}

export default HomepageLayout;
